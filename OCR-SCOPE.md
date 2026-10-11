# Sinica 29 與相關雜字書的公開 OCR 範圍查證

檢索日期：2026-10-11（UTC）。查證者：Codex AI。此紀錄只查書目、OCR 存在與涵蓋範圍，不轉載現代 OCR 正文，也不把搜尋結果當成逐頁校對成果。

## 結論與證據強度

本次查找未找到可確定屬於 Bodleian **Sinica 29、1586 年鄒少聰刊本**的公開 OCR／完整轉錄。館方公開 IIIF manifest 提供 32 個影像畫布，未連結文字層或 OCR 註釋；這只能證明該 manifest 未提供 OCR，不能證明世界上或館方其他系統中沒有轉錄。

相關清代雜字書已有中國哲學書電子化計劃（Ctext）自動 OCR：至少確認《增廣幼學須知鰲頭雜字大全》一個同名 OCR 章節，以及《增補素翁指掌雜著全集》的「一」「二」兩個 OCR 章節。這些是不同書／不同刊本的存在證據，不能代替 Sinica 29 的全冊影像轉錄。尚未核完其全部影像頁與 OCR 頁的對應，故不宣稱逐頁完整或已完成校對。

## 目標：Bodleian Sinica 29

- 館方物件頁：<https://digital.bodleian.ox.ac.uk/objects/c21ff2d1-5823-4c15-920c-38e44be2607f/>
- 館方 manifest：<https://iiif.bodleian.ox.ac.uk/iiif/manifest/c21ff2d1-5823-4c15-920c-38e44be2607f.json>
- 館方書目：<https://east-asian.bodleian.ox.ac.uk/catalog/volume_2621>

對工作區已取得的官方 manifest 進行結構檢查：`sequences[0].canvases` 共 32 項；32 項的 `otherContent` 均為空陣列；`images` 所繫結者為影像資源，未見文字資源；manifest 未設 `seeAlso`；唯一 `rendering` 是物件 HTML 頁。因此此 manifest 不是 OCR 資料集。

館方索引書目與 SERICA 書目記載書名《京傳新刊素翁鰲頭雜字附詩柬活套便覽》，一卷，佚名撰，明萬曆丙戌（1586）建陽書林鄒少聰刊，線裝一冊，24 公分。SERICA 條目中的「全文」須避免誤解：實際點擊連結進入 Bodleian IIIF Universal Viewer，屬全冊影像的閱讀入口，不是可下載文字的存在證據。

- SERICA 書目與「全文」入口：<https://serica.ie/SericaProject/data/630.html>（Sinica 29 條目）
- SERICA 數位化書目清單：<https://serica.ie/SericaProject/data/SPquanwen.html>
- 「全文」連結目的地：<https://iiif.bodleian.ox.ac.uk/iiif/viewer/c21ff2d1-5823-4c15-920c-38e44be2607f>

## 相關清代雜字書：已確認與仍待查

### 《增廣幼學須知鰲頭雜字大全》

**已確認：** Ctext 電子版索引明示自動 OCR，並提醒辨識會有錯誤。圖書館書目記載原書來源為哈佛燕京圖書館、掃描者為哈佛大學，並列出相關維基電子版。

- Ctext OCR 電子版：<https://ctext.org/wiki.pl?if=en&res=618785>
- 可識別的同名 OCR 章節：<https://ctext.org/wiki.pl?chapter=924411&if=en&remap=gb>
- Ctext 底本影像書目：<https://ctext.org/library.pl?if=en&res=94802>
- 中文介面書目：<https://ctext.org/library.pl?if=gb&res=94802>

**已確認的範圍：** 至少一個同名 OCR 電子版／章節存在。Ctext 中文索引亦顯示「清」。OCR 範圍初查沒有直接讀到完整目錄與逐頁影像／OCR 對應，故不計算總字數、總 OCR 頁數、正確率或百分比覆蓋。

**版本待查：** Ctext 索引所連哈佛底本的確切刊年、刊者及是否缺頁仍未直接核實。Wikimedia Commons 哈佛備份清單列有 `Harvard drs 52497185 增廣幼學須知鳌頭雜字大全.pdf`，但 OCR 範圍初查未能打開其單檔書目或哈佛 manifest。後續另一組 Codex AI 來源研究取得該影印副本作限定影像抽樣，見 [PROVENANCE.md](PROVENANCE.md)；這沒有完成它與 Ctext OCR 底本的逐頁同一性比對。不得逕把它標成其他網站所說的 1678 年瑯嬛閣《增補幼學須知雜字大全》；兩者題名不同。

- DRS 備份清單線索：<https://commons.wikimedia.org/wiki/Commons:Library_back_up_project/file_list/Harvard-Yenching/3>
- 待核實的哈佛閱讀入口：<https://iiif.lib.harvard.edu/manifests/view/drs:52497185>

### 《增補素翁指掌雜著全集》

**已確認：** Ctext 書目標示哈佛燕京圖書館來源、哈佛掃描，列「增補素翁指掌雜著全集一」「增補素翁指掌雜著全集二」兩冊影像，以及相關維基電子版。該維基電子版標明自動 OCR；「一」「二」兩個章節均標明自動 OCR。

- Ctext 底本影像書目：<https://ctext.org/library.pl?if=gb&res=94804>
- Ctext OCR 電子版：<https://ctext.org/wiki.pl?if=en&res=866080>
- OCR 章節「一」：<https://ctext.org/wiki.pl?chapter=432370&if=en>
- OCR 章節「二」：<https://ctext.org/wiki.pl?chapter=300265&if=en>

**版本區別：** 哈佛此本為清康熙八年（1669）書林千賦堂刊、兩冊，書目題李贄編、陳眉公（繼儒）選集、王百谷註釋。國家圖書館中文古籍聯合目錄對哈佛藏本亦記清康熙八年 1669；Wikimedia Commons 第二冊書目保留哈佛館藏 ID `990080869530203941`、DRS `52497186` 與底本描述。它距 Sinica 29 的刊年 83 年，題名、編選及內容結構不同，不能視為 Sinica 29 的 OCR 或缺字補本。

- 哈佛原始書目（本次直接讀取未成功）：<https://id.lib.harvard.edu/alma/990080869530203941/catalog>
- 哈佛原始數位閱讀入口：<https://iiif.lib.harvard.edu/manifests/view/drs:52497186>
- 國家圖書館中文古籍聯合目錄（書名：增補素翁指掌雜著全集；登錄號：tracy30008621；現藏者：哈佛燕京圖書館）：<https://rbook.ncl.edu.tw/NCLSearch/Search/SearchDetail?HasImage=&SourceID=3&item=ffdab7047a1349278572ee9eccd4e557fDg3OTAy0.hCOumFxL_Qdp7R1T_5X_fHB4nPN_HZBwJePssUhN9e0_&page=80242&sourceWhereString=&whereString=IChOVUxMSUYoRGF0ZV9DcmVhdGVkLCAnICcpIGlzIE5VTEwgYW5kIE5VTExJRihEb2N1bWVudF9ZZWFyLCAnICcpIGlzIE5VTEwgKSA1.uQrV5XxqrHh4fOCXMwOuuzssvPVRwJbumFyT4mFEUCA_>
- 可讀的第二冊書目副本：<https://commons.wikimedia.org/wiki/File:Harvard_drs_52497186_增補素翁指掌雜著全集_v.2.pdf>

**仍待查：** 兩個 OCR 章節與所有影像頁的逐頁對應、上欄圖文與下欄分類文字是否均涵蓋、書柬及契式是否完整、缺損及異體處理、OCR 後有多少人工更正。兩個章節的存在不等於這些項目已驗證。

## 查找範圍與限制

本次以公開網頁搜尋及館方 manifest 結構檢查查找：Sinica 29 shelfmark、完整與縮略中文題名、Bodleian object UUID，以及 OCR、transcription、轉錄等關鍵詞；並檢索 Ctext 的相關雜字書條目、館方書目／IIIF、SERICA 的書目與數位化入口。有效來源以館方或資料集自身記錄為主；備份站只作版本線索，不從其中搬取正文。

Ctext 的搜尋索引足以證實其 OCR 聲明及章節存在，但直接開啟相關頁在本次環境遇 403 Forbidden，單一書目請求亦逾時；哈佛書目／manifest 直接讀取未成功或回傳 403。未繞過存取限制，未登入，未批量抓取 Ctext 網頁。上述障礙限制了逐頁完整度驗證。

沒有查遍所有付費資料庫、未索引網站、私人研究檔案或館方內部資料。因此本紀錄的否定結論限定為「在以上公開查找範圍內，未找到可確定對應 Sinica 29 的 OCR／完整轉錄」。不得寫成「全球尚無 OCR」「首次轉錄」或「唯一電子版」。本次 Sinica 29 成果仍應以官方原圖自行逐字轉錄及獨立影像複核，不抄錄以上現代 OCR，也不以相關刊本推測原圖讀不清的字。
