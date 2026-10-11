# Sinica 29｜1586年《鰲頭雜字》逐頁AI影像轉錄

以Bodleian Library Sinica 29為底本，轉錄《京傳新刊素翁鰲頭雜字附詩柬活套便覽》（佚名，1586年建陽鄒少聰刊）。全部32畫布均經初錄與另一位AI重新看圖複核，涵蓋fol. 1r–12v的24面正文及8張封面／襯葉。上下欄、細字、題署、詩柬欄序與來源定位分開保存。

整理與維護：**poplolioi11／一卦 [yigua.art](https://yigua.art/)**。這是AI影像轉錄及獨立AI複核，仍有未解字，**不是人工專家校勘或無誤定本**。本次非商業整理，僅發布自己核讀的文字、結構與說明；原圖仍由[Digital Bodleian](https://digital.bodleian.ox.ac.uk/objects/c21ff2d1-5823-4c15-920c-38e44be2607f/)提供。詳細版本與方法見[PROVENANCE.md](PROVENANCE.md)。

## 已完成範圍與未解字

| 項目 | 數量與限制 |
| --- | --- |
| 影像覆蓋 | 32/32畫布；24/24編號正文面；每面初錄與複核固定工作流ID不同 |
| 數位定位行 | 734條，含正文、細字、標題、印章及後人書寫；不是原書總行數 |
| 既有行複核修正 | 239筆；corrections.json只列既有行修正 |
| 複核新增／刪除 | 新增10區、11條定位行；刪除0行 |
| 題署／上下欄／邊記未解□ | 234個（題署、上下欄及版心／邊欄；邊記中含1個印刷或後寫性質未定的黑記號） |
| 印章／後人書寫未解□ | 30個，與正文分開 |
| 全部未解□ | 264個；不含字數不明缺損的未知字數 |
| 字數不明缺損 | 27段；不可折算成字數 |
| 疑字定位紀錄 | 291筆，詳見uncertainties.json；含單字疑讀與缺損範圍 |

「完整覆蓋」指本次數位畫布全部處理，不表示每個字已定讀或藏本從無缺損。□是一個未定讀字位；〔缺損字數不明〕不能折算成可靠字數或辨識率。候選只存疑字紀錄，不把推測寫入正文。沒有以後出清刊本、模型記憶或網路通行文字補字。

## 檔案

- [sinica-29.json](sinica-29.json)：32面逐區逐欄文字、近似框選、頁記、來源及獨立複核紀錄。
- [sinica-29.txt](sinica-29.txt)：由同一JSON匯出，便於閱讀；新增括號標題及行號與原文有明確界線。
- [coverage.json](coverage.json)：逐面覆蓋、初錄／複核者與未解字計數。
- [uncertainties.json](uncertainties.json)：未解字、候選、影像原因與頁行定位。
- [corrections.json](corrections.json)：複核改前、改後及理由。
- [VALIDATION.json](VALIDATION.json)、[SHA256SUMS](SHA256SUMS)：結構與完整性驗證結果及資料雜湊。
- [OCR-SCOPE.md](OCR-SCOPE.md)：既有相關OCR的限定查核與尚未確認的覆蓋項目。
- [LICENSE.md](LICENSE.md)、[CITATION.cff](CITATION.cff)、[CONTRIBUTING.md](CONTRIBUTING.md)：權利、引用及修正方式。

## 格式與定位

UTF-8，`schemaVersion: "1.0"`。JSON的`meta`存底本與整理資訊，`pages`依manifest順序排列。每頁的`regions`區分title、upper、lower、margin、seal與annotation，古籍直欄的`lines`按右至左欄序，欄內由上至下；後人橫書依原行順序。小字雙行與詩柬分行另存，不合成現代散文；不自行新增句讀。

| 欄位 | 用法 |
| --- | --- |
| `canvasIndex`、`label` | 1起算畫布序號及官方fol.標籤；正文是畫布5–28 |
| `source` | 固定官方畫布映射、影像服務、所檢查2400px影像尺寸與SHA-256；不含影像 |
| `review.sourceReviewed` | 實際複核原圖URL、尺寸及本機檔SHA-256；部分複核另看以3500px請求的高解析原圖，實際像素尺寸另記；公開驗證離線，不冒充網路驗證 |
| `transcriberAgentId`、`reviewerAgentId`與`taskId` | 由已記錄工作流任務名稱分配的固定身份；不構成密碼學或模型獨立性保證 |
| `regions[].id/kind/description` | 版面區別；分類題保留其原位置 |
| `lines[].id/order/text` | 全書唯一定位、區內欄序、原字文字；不做全域簡繁轉換 |
| `lines[].bbox` | 寬2400px檢查影像中近似[x,y,width,height]欄框，不是逐字精確座標 |
| `lines[].uncertainties` | Unicode碼點的0起算offset、length、kind、候選及原因 |
| `pageNotes`、`review` | `pageNotes`保留初錄歷史頁記，可能含當時待複核語句；最終複核見`review`與行內`uncertainties`。`line.note`原則上保留初錄行記，由`afterNote`或新增行替換者為複核行記。TXT分別標示來源；均非古籍正文 |

每面最終狀態`ai-image-reviewed-with-uncertainties`只表示已進行所記錄的AI讀圖與複核。部分影像仍淡損；模型一致不構成字形證據。不同刊本有相似詞表與後人OCR，本庫不主張首次數位化、首創內容或全球唯一電子版。

## 驗證與版本

- **v0.1.0**：原發布包為733條定位行、248個□；保留[原標籤](https://github.com/poplolioi11/sinica-29-zazi/tree/v0.1.0)及[原Release入口](https://github.com/poplolioi11/sinica-29-zazi/releases/tag/v0.1.0)。
- **v0.1.1（本次校讀版本）**：只針對10v字形分歧重新看圖，夜螢改夜蚤、踏缸改踏坯；18個原定讀字回置□，斜朱印原3個□改整印字數不明，新增性質未定邊記1個□。初錄歷史頁／行記的來源標籤更明確，其他31頁古籍文字不變；本版為734條定位行、264個□。見[v0.1.1 Release入口](https://github.com/poplolioi11/sinica-29-zazi/releases/tag/v0.1.1)。

2026-10-11已核實v0.1.1為GitHub公開正式Release，下載ZIP與Zenodo封存包逐位元組相同；固定提交與雜湊見下方引用及PROVENANCE。

Python 3，無第三方套件：

```sh
python3 verify.py
```

檢查固定32畫布與24面葉序、非空上下欄、不同工作流身份、初錄行區與複核操作整合、唯一定位、欄框與疑字偏移、JSON/TXT及三份派生紀錄一致性、五資料檔雜湊、公開檔白名單、UTF-8及私人路徑／影像排除。建置另核工作區32張原圖實體雜湊、sips尺寸與複核來源記錄。公開verifier為離線驗證，不替代原圖字形判讀，不保證外部URL永遠可用。TXT可用`python3 export_txt.py`重新匯出。

引用時記錄完整Git提交識別碼、所用資料檔SHA-256與取用日期；`main`會隨校訂更新。資料集引用為「poplolioi11（一卦 yigua.art），Sinica 29：1586年《京傳新刊素翁鰲頭雜字附詩柬活套便覽》AI影像轉錄，2026」，附本庫URL及版本。另引古籍作者／刊本及Bodleian原頁，不能把整理者當成古籍作者。

Zenodo於2026-10-11公開封存v0.1.1：[版本DOI 10.5281/zenodo.23299558](https://doi.org/10.5281/zenodo.23299558)固定此版；[概念DOI 10.5281/zenodo.23299557](https://doi.org/10.5281/zenodo.23299557)代表全版本。存檔包與GitHub v0.1.1原始發布ZIP相同，包內CITATION為發布前版本、尚無DOI；本庫文件現補登DOI。固定提交與ZIP雜湊見[PROVENANCE.md](PROVENANCE.md)。

## 權利

古代原文與忠實轉錄不另設新使用限制；自願保留來源及整理署名便於追溯。館方影像的CC BY-NC 4.0仍獨立適用，此庫不再散布影像。具原創性的新寫說明及資料編排貢獻，在適用權利範圍內採CC BY 4.0；兩支程式採MIT。完整範圍見[LICENSE.md](LICENSE.md)。不暗示館方背書。

## English summary

Image-based AI transcription of the 1586 Jianyang edition held as Bodleian Library Sinica 29. All 32 digital canvases, including the 24 numbered text pages, were read and independently reviewed by another AI reader. Upper and lower registers, small text, uncertain readings and source locations are retained. This is not expert human collation. The repository distributes authored text and structure, not scan images or modern OCR. Ancient text, institutional images, original documentation and code have separately stated rights in LICENSE.md.
