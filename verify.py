"""Offline integrity gates for authored text; no network or philological proof."""
import hashlib
import json
import math
import re
import sys
from pathlib import Path
sys.dont_write_bytecode = True
from export_txt import render

ROOT = Path(__file__).resolve().parent
CANVASES = (
 ('850e4451-c2a4-477f-a2ab-62872623b0c0','Upper cover'),
 ('6238aa9d-d9e1-48d4-a1f0-5715b4003073','Inside upper cover'),
 ('e8006ba9-f592-48e3-90e6-2ec1aceb4df2','Upper flyleaf recto'),
 ('f3bffdfe-48de-4f97-975a-ef7448dea005','Upper flyleaf verso'),
 ('7eb14bc2-221e-4f05-8bc4-adcfdd3c97d6','fol. 1r'),
 ('4bd935f7-f274-4d13-8634-60ed5fb589ce','fol. 1v'),
 ('86d9360f-b976-4ef2-bb48-fdd4f70eaf21','fol. 2r'),
 ('0b3b3fce-3c71-4a20-9e0f-bd8db3b62d62','fol. 2v'),
 ('6ec23979-e6a7-45f8-82e3-cbf9ff135b6c','fol. 3r'),
 ('0899c651-3b8d-4afc-bd67-6d38141d97b7','fol. 3v'),
 ('3bad70c4-acff-4107-b206-99ae0dc15d6f','fol. 4r'),
 ('45f29d35-1446-4c83-af64-cde5d12e39da','fol. 4v'),
 ('5f5a206a-89a8-4325-aa13-82d156e0d6c8','fol. 5r'),
 ('253e9dd5-cf71-4536-8048-9f7d7722c8ba','fol. 5v'),
 ('7f17f061-2319-4672-8cc8-957c7158e53e','fol. 6r'),
 ('99a4a483-d455-4681-b782-45090561790b','fol. 6v'),
 ('4764249d-90ee-45be-9cc0-557caa60be44','fol. 7r'),
 ('c2ef10d0-f05a-423d-bdfa-98fcaaf9b295','fol. 7v'),
 ('1623500a-93c9-4105-ab57-6b236b2fe0a8','fol. 8r'),
 ('1f36446a-87ff-4389-9151-605f211d6bd4','fol. 8v'),
 ('69ce66e8-9578-41cf-ac9e-f4686261076d','fol. 9r'),
 ('200c0825-27f4-428a-a2b4-3a761fec5927','fol. 9v'),
 ('4d8ac34a-1abe-45a7-9594-b86a187ee84b','fol. 10r'),
 ('e2cf6ec8-acdf-4b5c-b688-251d4c467aa6','fol. 10v'),
 ('142abcdb-782f-43b5-b428-4fa09f4259cb','fol. 11r'),
 ('83eba8e0-4d45-498b-8aad-ea52491e35d3','fol. 11v'),
 ('2b5ee20f-fe0d-4a1b-9bc8-a5662de0751e','fol. 12r'),
 ('46e1961d-1b85-42bd-b7bb-8b5852c7d953','fol. 12v'),
 ('06e9caa3-060b-476e-967a-3bb849140158','Lower flyleaf recto'),
 ('183730a9-b2f8-4474-9c4e-93d80acc9fd1','Lower flyleaf verso'),
 ('3c39b480-4694-4504-8d9a-baf38119521c','Inside lower cover'),
 ('283f7e97-08bc-46c9-8d56-18d46d3d5cd8','Lower cover'))
AGENTS = {f'Codex AI / {name}': {'agentId':f'codex:sinica29:2026-10-11:{name}', 'taskId':f'/root/{name}' if name != 'root' else '/root'}
          for name in ('transcribe_a','transcribe_b','transcribe_c','transcribe_d','transcribe_e','ocr_scope','root','review_10v')}
AGENTS['Codex AI / agent transcribe_e'] = AGENTS['Codex AI / transcribe_e']
DATA_FILES = {'sinica-29.json','sinica-29.txt','coverage.json','uncertainties.json','corrections.json'}
REQUIRED_DOCUMENTS = {'README.md','LICENSE.md','CITATION.cff','PROVENANCE.md','OCR-SCOPE.md','CONTRIBUTING.md','verify.py','export_txt.py'}
PUBLIC_FILES = DATA_FILES | {'README.md','LICENSE.md','CITATION.cff','PROVENANCE.md','OCR-SCOPE.md','CONTRIBUTING.md','VALIDATION.json','SHA256SUMS','verify.py','export_txt.py','.gitignore'}
KINDS = {'title','upper','lower','margin','seal','annotation'}
SHA = re.compile(r'[0-9a-f]{64}\Z')
PRIVATE = re.compile(r'file://(?=/|[A-Za-z]:)|/(?:Users|home|tmp|private|var/folders|Volumes|mnt)/|(?<![A-Za-z0-9])[A-Za-z]:[\\/]',re.I)

class ValidationError(ValueError):
    pass

def require(ok, message):
    if not ok:
        raise ValidationError(message)

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def safe_value(value, location='data'):
    if isinstance(value,str):
        require(not PRIVATE.search(value),f'Private filesystem path in {location}')
        require(not re.search(r'data:(?:image/|application/pdf)',value,re.I),f'Embedded image/PDF in {location}')
    elif isinstance(value,dict):
        for k,v in value.items(): safe_value(v,f'{location}.{k}')
    elif isinstance(value,list):
        for i,v in enumerate(value): safe_value(v,f'{location}[{i}]')

def identity(display):
    require(display in AGENTS,'Unknown workflow reader identity: '+str(display))
    return AGENTS[display]

def source_mapping(index):
    require(type(index) is int and 1 <= index <= 32,'Invalid canvas index')
    uuid,label = CANVASES[index-1]
    service = 'https://iiif.bodleian.ox.ac.uk/iiif/image/'+uuid
    return {'label':label,'canvas':'https://iiif.bodleian.ox.ac.uk/iiif/canvas/'+uuid+'.json','imageService':service,'imageUrl':service+'/full/2400,/0/default.jpg'}

def final_note(value):
    return value.replace('待獨立影像複核','獨立影像複核後仍未定讀')

def final_uncertainties(items):
    return [{**u,'note':final_note(u['note'])} for u in items]

def check_line(line, source, context):
    require(isinstance(line['id'],str) and bool(line['id']),context+': empty line ID')
    text=line['text']
    require(isinstance(text,str) and bool(text.strip()) and '\ufffd' not in text,context+': empty/invalid text')
    box=line['bbox']
    require(isinstance(box,list) and len(box)==4 and all(type(v) in (int,float) and math.isfinite(v) for v in box),context+': invalid bbox')
    require(box[0]>=0 and box[1]>=0 and box[2]>0 and box[3]>0,context+': invalid bbox extent')
    require(box[0]+box[2]<=source['inspectedImageWidth']+2 and box[1]+box[3]<=source['inspectedImageHeight']+2,context+': bbox outside image')
    marked=set()
    for u in line['uncertainties']:
        require(set(u)<= {'offset','length','kind','candidates','note'},context+': unexpected uncertainty key')
        o,n=u['offset'],u['length']
        require(type(o) is int and type(n) is int and n>0 and 0<=o<len(text) and o+n<=len(text),context+': invalid uncertainty offset')
        require(u['kind'] in {'unclear','damaged','unencoded'} and isinstance(u['note'],str) and bool(u['note'].strip()),context+': invalid uncertainty reason')
        require(isinstance(u.get('candidates',[]),list) and all(isinstance(c,str) for c in u.get('candidates',[])),context+': invalid candidates')
        require('待獨立影像複核' not in u['note'],context+': stale review-pending note')
        marked.update(range(o,o+n))
    require(all(i in marked for i,c in enumerate(text) if c=='□'),context+': unlocated □')

def validate_operations(page):
    review=page['review']
    first=review['firstPassStructure']
    require(isinstance(first,list),'Missing first-pass structure')
    original={}; initial_lines={}
    for r in first:
        require(r['id'] not in original and r['kind'] in KINDS,'Duplicate/invalid original region')
        require(isinstance(r['lineIds'],list) and len(set(r['lineIds']))==len(r['lineIds']),'Duplicate original line IDs')
        original[r['id']]=r
        for lid in r['lineIds']:
            require(lid not in initial_lines,'Repeated original line ID')
            initial_lines[lid]=r['id']
    require(SHA.fullmatch(review['firstPassSha256']) is not None,'Invalid first-pass file hash')
    final_regions={r['id']:r for r in page['regions']}
    final_lines={l['id']:(r['id'],l) for r in page['regions'] for l in r['lines']}
    removed=review.get('removeLineIds',[])
    require(len(set(removed))==len(removed) and set(removed)<=set(initial_lines),'Invalid/duplicate removed line ID')
    added={}; added_regions={}
    for a in review.get('addLines',[]):
        rid=a['regionId'];lid=a['line']['id']
        require(rid in original and lid not in initial_lines and lid not in added,'Invalid added line target/ID')
        added[lid]=(rid,a['line'])
    for r in review.get('addRegions',[]):
        require(r['id'] not in original and r['id'] not in added_regions,'Duplicate added region ID')
        added_regions[r['id']]=r
        for line in r['lines']:
            require(line['id'] not in initial_lines and line['id'] not in added,'Duplicate added region line ID')
            added[line['id']]=(r['id'],line)
    require(set(final_regions)==set(original)|set(added_regions),'Missing/unrecorded final region')
    require(set(final_lines)==(set(initial_lines)-set(removed))|set(added),'Missing/unrecorded final line')
    for rid,r in original.items(): require(final_regions[rid]['kind']==r['kind'],'Original region kind changed')
    for lid,rid in initial_lines.items():
        if lid not in removed: require(final_lines[lid][0]==rid,'Original line moved without operation')
    for rid,r in added_regions.items():
        for key in ('kind','description'): require(final_regions[rid][key]==r[key],'Added region not integrated: '+rid)
    for lid,(rid,line) in added.items():
        require(final_lines[lid][0]==rid,'Added line in wrong region: '+lid)
        expected={k:v for k,v in line.items() if k!='order'}
        if 'uncertainties' in expected: expected['uncertainties']=final_uncertainties(expected['uncertainties'])
        require({k:v for k,v in final_lines[lid][1].items() if k!='order'}==expected,'Added line not integrated: '+lid)
    corrected=set()
    for c in review.get('corrections',[]):
        require(set(c)<= {'lineId','before','after','afterUncertainties','afterNote','afterBbox','reason'},'Unexpected correction key')
        lid=c['lineId']
        require(lid in initial_lines and lid not in corrected,'Invalid/duplicate correction ID')
        require(isinstance(c['before'],str) and isinstance(c['after'],str) and bool(c.get('reason')),'Invalid correction evidence')
        corrected.add(lid)
        require(c['before']==c['after'] or 'afterUncertainties' in c,'Changed text without uncertainty replacement')
        if lid in removed: continue
        l=final_lines[lid][1]
        require(l['text']==c['after'],'Correction text not integrated: '+lid)
        for key,target in [('afterUncertainties','uncertainties'),('afterNote','note'),('afterBbox','bbox')]:
            if key in c:
                expected=final_uncertainties(c[key]) if key=='afterUncertainties' else c[key]
                require(l.get(target)==expected,'Correction field not integrated: '+lid+'/'+target)

def validate_data(data):
    safe_value(data)
    require(data['schemaVersion']=='1.0','Unexpected schema version')
    pages=data['pages']
    require(len(pages)==32 and [p['canvasIndex'] for p in pages]==list(range(1,33)),'Expected exactly canvases 1–32 in order')
    ids=set(); seen_sources=set()
    for p in pages:
        i=p['canvasIndex'];mapping=source_mapping(i);s=p['source'];rev=p['review']
        require(p['label']==mapping['label'],'Wrong label at canvas '+str(i))
        for k in ('canvas','imageService'): require(s[k]==mapping[k],'Wrong source '+k+' at canvas '+str(i))
        require(s['canvas'] not in seen_sources,'Duplicate source canvas');seen_sources.add(s['canvas'])
        require(s['isNumberedLeaf'] is (5<=i<=28),'Wrong numbered-leaf flag')
        require(s['inspectedImageUrl']==mapping['imageUrl'],'Wrong 2400px inspection URL')
        require(type(s['inspectedImageWidth']) is int and s['inspectedImageWidth']==2400 and type(s['inspectedImageHeight']) is int and s['inspectedImageHeight']>0,'Invalid inspection dimensions')
        require(SHA.fullmatch(s['inspectedImageSha256']) is not None,'Invalid inspected-image SHA-256')
        tid=identity(p['transcriber']);rid=identity(rev['reviewer'])
        require(p['transcriberAgentId']==tid['agentId'] and p['transcriberTaskId']==tid['taskId'],'Transcriber stable identity mismatch')
        require(rev['reviewerAgentId']==rid['agentId'] and rev['reviewerTaskId']==rid['taskId'],'Reviewer stable identity mismatch')
        require(tid['agentId']!=rid['agentId'] and tid['taskId']!=rid['taskId'],'Self-review is not independent')
        require(rev['reviewedAllLines'] is True and p['status']=='ai-image-reviewed-with-uncertainties','Unfinished review')
        require('imagePaths' not in rev,'Private review imagePaths retained')
        viewed=rev['sourceReviewed']; widths=[]
        for image in viewed:
            width=image['width'];requested=image['requestedWidth'];widths.append(requested)
            require(type(requested) is int and requested in (2400,3500) and type(width) is int and 0<width<=requested,'Unexpected reviewed image request/actual width')
            require(image['url']==s['imageService']+f'/full/{requested},/0/default.jpg','Wrong reviewed-source URL')
            require(type(image['height']) is int and image['height']>0 and SHA.fullmatch(image['sha256']) is not None,'Invalid reviewed-image evidence')
            require(image['evidence']=='local-file-hash-and-dimensions; source mapping from saved inventory/review record; no network verification','Unknown review evidence basis')
            if requested==2400: require(width==2400 and image['sha256']==s['inspectedImageSha256'] and image['height']==s['inspectedImageHeight'],'Reviewed base image differs')
            else: require(width>2400 and abs(image['height']/width-s['inspectedImageHeight']/2400)<0.002,'Reviewed high-resolution dimensions differ')
        required_widths={2400,3500} if rid['agentId']==AGENTS['Codex AI / transcribe_d']['agentId'] else {2400}
        require(len(widths)==len(set(widths)) and required_widths<=set(widths)<= {2400,3500},'Missing/unsupported actually reviewed image resolution')
        require(rev['imagesReviewed']==[im['url'] for im in viewed],'Reviewed URL list differs from evidence')
        for crop in rev.get('cropEvidence',[]):
            require(crop['canvasIndex']==i and SHA.fullmatch(crop['sha256']) is not None and type(crop['width']) is int and crop['width']>0 and type(crop['height']) is int and crop['height']>0,'Invalid working crop evidence')
        regionids=set()
        if 5<=i<=28:
            for kind in ('upper','lower'):
                require(any(r['kind']==kind and len(r['lines'])>0 for r in p['regions']),'Empty/missing '+kind+' at canvas '+str(i))
        for r in p['regions']:
            require(r['id'] not in regionids and r['kind'] in KINDS,'Duplicate/invalid region');regionids.add(r['id'])
            require([l['order'] for l in r['lines']]==list(range(1,len(r['lines'])+1)),'Nonconsecutive line order')
            for l in r['lines']:
                require(l['id'] not in ids,'Duplicate global line ID: '+l['id']);ids.add(l['id'])
                check_line(l,s,l['id'])
        validate_operations(p)
    return data

def derive_uncertainties(data):
    return [{'canvasIndex':p['canvasIndex'],'label':p['label'],'regionId':r['id'],'lineId':l['id'],**u} for p in data['pages'] for r in p['regions'] for l in r['lines'] for u in l['uncertainties']]

def derive_corrections(data):
    return [{'canvasIndex':p['canvasIndex'],'reviewer':p['review']['reviewer'],'reviewerAgentId':p['review']['reviewerAgentId'],'reviewerTaskId':p['review']['reviewerTaskId'],**c} for p in data['pages'] for c in p['review'].get('corrections',[])]

def derive_coverage(data):
    pages=data['pages'];linecount=lambda p:sum(len(r['lines']) for r in p['regions'])
    count=lambda kinds:sum(l['text'].count('□') for p in pages for r in p['regions'] if r['kind'] in kinds for l in r['lines'])
    return {'canvasCount':len(pages),'numberedPageCount':sum(p['source']['isNumberedLeaf'] for p in pages),
      'reviewedCanvasCount':sum(p['review']['reviewedAllLines'] is True for p in pages),'lineCount':sum(linecount(p) for p in pages),
      'unresolvedPlaceholderCount':count(KINDS),'scopeLimitation':'Complete coverage of the supplied digital canvases; unresolved readings remain.',
      'pages':[{'canvasIndex':p['canvasIndex'],'label':p['label'],'transcriber':p['transcriber'],'transcriberAgentId':p['transcriberAgentId'],'transcriberTaskId':p['transcriberTaskId'],
        'reviewer':p['review']['reviewer'],'reviewerAgentId':p['review']['reviewerAgentId'],'reviewerTaskId':p['review']['reviewerTaskId'],'status':p['status'],
        'regions':len(p['regions']),'lines':linecount(p),'unresolvedPlaceholders':sum(l['text'].count('□') for r in p['regions'] for l in r['lines'])} for p in pages],
      'unresolvedAncientTextPlaceholders':count({'title','upper','lower','margin'}),'unresolvedLaterMarkPlaceholders':count({'seal','annotation'}),
      'independentCorrections':len(derive_corrections(data)), 'independentCorrectionsScope':'Existing line correction records only; additions/removals counted separately.',
      'reviewAddLineCount':sum(len(p['review'].get('addLines',[]))+sum(len(r['lines']) for r in p['review'].get('addRegions',[])) for p in pages),
      'reviewAddRegionCount':sum(len(p['review'].get('addRegions',[])) for p in pages),'reviewRemoveLineCount':sum(len(p['review'].get('removeLineIds',[])) for p in pages)}

def validate_tree(root):
    root=Path(root)
    git=root/'.git'
    require(not git.is_symlink(),'.git symlink is not allowed')
    for p in root.rglob('*'):
        rel=p.relative_to(root)
        if rel.parts[0]=='.git': continue  # Local Git metadata is not a published artifact.
        require(not p.is_symlink(),'Symlink in publication tree: '+str(rel))
        require(p.is_file() and len(rel.parts)==1 and rel.name in PUBLIC_FILES,'Unexpected publication artifact: '+str(rel))
        raw=p.read_bytes()
        require(not raw.startswith((b'\xff\xd8\xff',b'\x89PNG',b'GIF87a',b'GIF89a',b'II*\x00',b'MM\x00*',b'%PDF-',b'RIFF')),'Image/PDF binary in publication: '+str(rel))
        try: content=raw.decode('utf-8')
        except UnicodeDecodeError as exc: raise ValidationError('Non-UTF-8 public artifact: '+str(rel)) from exc
        safe_value(content,str(rel))

def verify(root=None, require_documents=True):
    root=Path(root) if root is not None else ROOT
    validate_tree(root)
    if require_documents:
        require(all((root/n).is_file() for n in REQUIRED_DOCUMENTS),'Missing required release document/program')
    data=validate_data(json.loads((root/'sinica-29.json').read_text(encoding='utf-8')))
    require((root/'sinica-29.txt').read_text(encoding='utf-8')==render(data),'JSON/TXT mismatch')
    checks=[]
    for row in (root/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        require(re.fullmatch(r'[0-9a-f]{64}  [A-Za-z0-9_.-]+',row) is not None,'Malformed SHA256SUMS entry')
        h,name=row.split('  ',1)
        require(name in DATA_FILES and name not in checks,'Unknown/duplicate hash entry: '+name)
        require(sha256(root/name)==h,'Data-file hash mismatch: '+name);checks.append(name)
    require(set(checks)==DATA_FILES,'All five data files must have hashes')
    require(json.loads((root/'coverage.json').read_text())==derive_coverage(data),'Coverage differs from final JSON')
    require(json.loads((root/'uncertainties.json').read_text())==derive_uncertainties(data),'Uncertainties differ from final JSON')
    require(json.loads((root/'corrections.json').read_text())==derive_corrections(data),'Corrections differ from page reviews')
    coverage=derive_coverage(data)
    return {'result':'pass','canvases':coverage['canvasCount'],'numberedPages':coverage['numberedPageCount'],'reviewedCanvases':coverage['reviewedCanvasCount'],
      'lines':coverage['lineCount'],'codePointsInTranscribedLines':sum(len(l['text']) for p in data['pages'] for r in p['regions'] for l in r['lines']),
      'unresolvedPlaceholders':coverage['unresolvedPlaceholderCount'],'checkedHashes':checks,
      'limitation':'Offline structure, operation integration and file integrity only; source/reader mapping is recorded workflow evidence, not network verification or proof of every reading.'}

if __name__=='__main__':
    try: print(json.dumps(verify(),ensure_ascii=False,indent=2))
    except (ValidationError,KeyError,ValueError,OSError,TypeError) as exc:
        print(f'FAIL: {exc}',file=sys.stderr);sys.exit(1)
