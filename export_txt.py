"""Render the reading TXT deterministically from the authored JSON; no OCR."""
import json
from pathlib import Path

def render(data):
    out = [data['meta']['catalogueTitle'], '底本：Bodleian Library Sinica 29（1586）',
           '整理署名：poplolioi11／一卦 yigua.art',
           'AI影像轉錄與獨立AI複核；□表示未解字。〔〕與行號為數位編輯標記。',
           '古籍直欄按右到左欄序、欄內上到下；後人橫書依原行順序。標題、上下欄、印章及後人書寫分區。', '']
    for p in data['pages']:
        out += [f"〔畫布 {p['canvasIndex']:02}｜{p['label']}〕", p['source']['canvas']]
        for r in p['regions']:
            out += [f"〔區 {r['id']}｜{r['kind']}｜{r['description']}〕"]
            out += [f"{l['id']}\t{l['text']}" for l in r['lines']]
        if not p['regions']:
            out += ['〔本面無可辨認的獨立正文；見頁面紀錄〕']
        out += ['']
    out += ['〔編輯紀錄；以下非古籍正文〕']
    for p in data['pages']:
        out += [f"〔畫布 {p['canvasIndex']:02}｜{p['label']}〕"]
        out += [f"初錄頁記（最終複核見JSON的review）：{n}" for n in p['pageNotes']]
        review=p['review']
        reviewed_note_ids={c['lineId'] for c in review.get('corrections',[]) if 'afterNote' in c}
        reviewed_note_ids.update(a['line']['id'] for a in review.get('addLines',[]))
        reviewed_note_ids.update(l['id'] for r in review.get('addRegions',[]) for l in r['lines'])
        for r in p['regions']:
            for l in r['lines']:
                basis='複核行記' if l['id'] in reviewed_note_ids else '初錄行記（最終複核見JSON的review）'
                if l.get('note'): out += [f"{l['id']} {basis}：{l['note']}"]
                for u in l['uncertainties']:
                    out += [f"{l['id']} 疑字 offset={u['offset']} length={u['length']}：{u['kind']}；候選={'、'.join(u.get('candidates', []))}；{u['note']}"]
        out += ['']
    return '\n'.join(out).rstrip() + '\n'

if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    data = json.loads((root / 'sinica-29.json').read_text(encoding='utf-8'))
    (root / 'sinica-29.txt').write_text(render(data), encoding='utf-8')
