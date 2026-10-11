# 來源、方法與權利紀錄

## 底本

《京傳新刊素翁鰲頭雜字附詩柬活套便覽》，佚名撰，明萬曆丙戌（1586）建陽書林鄒少聰刊，一卷一冊。藏本為 Bodleian Libraries, University of Oxford，Sinica 29。書目題名依 [SERICA 目錄](https://serica.ie/SericaProject/data/630.html)；年代與版本另見 [早期入歐漢籍目錄](https://serica.ie/17thcent/17theu.html)。JSON 的正文題字依各面原圖另存，不以書目文字覆蓋原刻。

- [Digital Bodleian 藏本入口](https://digital.bodleian.ox.ac.uk/objects/c21ff2d1-5823-4c15-920c-38e44be2607f/)
- [官方 IIIF manifest](https://iiif.bodleian.ox.ac.uk/iiif/manifest/c21ff2d1-5823-4c15-920c-38e44be2607f.json)
- [官方完整書目入口](https://east-asian.bodleian.ox.ac.uk/catalog/volume_2621)（本次直接讀取遇到安全檢查，未繞過；版本資料由上述目錄及原刻首尾題署交叉核實。）

取用與處理日：2026-10-11。收尾時重新讀取官方manifest得到HTTP 200，核對全部32畫布的ID、標籤、影像服務與順序，均與保存清單一致；這不等於重新下載或逐字核對所有來源影像。manifest 為32畫布：4張前封面／襯葉、fol. 1r–12v共24面、4張後襯葉／封面。全32張下載之2400px寬JPEG可解碼，SHA-256各異；來源與雜湊見JSON。這能說明此次數位影像覆蓋，不能證明藏本歷史上從無缺損。淡印、磨損、透印、印章與後人書寫見逐頁紀錄。

## 轉錄與複核

直接從本藏本影像逐字閱讀，由Codex AI分組初錄，另由未初錄該面之Codex AI重新開啟原圖逐行複核；不是人工專家校勘。各頁保留初錄者、複核者與修改紀錄。沒有複製現代OCR、標點本、翻譯或註釋。初稿與複核工作的內部影像不隨公開資料發布。

下欄雜字、上欄詩柬、跨欄標題、細字選詞、藏印及後人書寫分區；欄序右至左、欄內上至下。欄識別碼與近似框選為整理者新增定位，非原書行號或逐字精準座標。可編碼異體保留，不做全域簡繁轉換。未能定讀者留「□」及候選與影像原因；字數無法確定的缺損另明記。疑字偏移以Unicode碼點、從0起算，不是UTF-8位元組或JavaScript UTF-16索引。印章與後人書寫不混入古籍正文；透印只作頁記。

TXT由JSON確定性匯出，標題括號、欄號及編輯紀錄均為閱讀標記。程式只檢查結構、覆蓋、疑字定位、JSON/TXT一致性及雜湊；不能證明讀法正確。未解字清單含正文與附記，兩者須分別評估。

## 相關版本及現成OCR

限定查核未找到可確定直接覆蓋Sinica 29全部24面的現成轉錄。官方manifest沒有OCR文字層；SERICA的「全文」連到影像閱讀器。這不是全球不存在OCR的證明。

中國哲學書電子化計劃有後出相關本之自動OCR：[《增補素翁》](https://ctext.org/wiki.pl?if=en&res=866080)、[《增廣幼學》](https://ctext.org/wiki.pl?if=gb&res=618785)。直接取讀遇安全檢查及可能混入錯字提示；未繞過、未將搜尋摘要字串作校讀依據，逐頁OCR完整度尚未核實。具體檢索範圍見 [OCR-SCOPE.md](OCR-SCOPE.md)。

另一次來源研究作限定影像抽樣，比對哈佛藏1669《增補素翁指掌雜著全集》與《增廣幼學須知鰲頭雜字大全》的公開影印副本：[1669本](https://commons.wikimedia.org/wiki/File:Harvard_drs_52497186_增補素翁指掌雜著全集_v.1.pdf)、[DRS 52497185本](https://commons.wikimedia.org/wiki/File:Harvard_drs_52497185_增廣幼學須知鳌頭雜字大全.pdf)。Sinica 29的9r與前者PDF第5頁左半、後者第18頁左半有魚類詞重合；3r與1669本PDF第14頁左半有器物詞重合。各本次序、增刪、細注及上欄不同。這項抽樣由委派Codex AI來源研究員報告，未用於填補本文疑字，也不能推算全書異同百分比。DRS 52497185影印副本與Ctext OCR底本的同一性尚未完成逐頁核實。本資料價值是此1586版的逐頁文字、異體、次序與詩柬見證，不主張內容全新或首創。

## 適用權利與用途

官方manifest標示影像「Photo: © Bodleian Libraries, University of Oxford」，[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。[館方terms](https://digital.bodleian.ox.ac.uk/terms/)容許非商業研究與不推廣商業活動的研究網站／資料庫。本次非商業讀圖研究符合該項用途；公開成果僅含獨立轉錄、結構與來源連結，不散布掃描、裁圖或館方標誌。

古代原文、館方影像與新寫說明分開處理，見 [LICENSE.md](LICENSE.md)。CC條款對不受其授權權利約束的公版成分不另設限制，參考 [legalcode第1、2、8節](https://creativecommons.org/licenses/by-nc/4.0/legalcode.en)。此為對本次用途的有來源判斷，不是所有法域、未來用途或其他館藏的法律保證。未對館方外聯，也不暗示館方背書。
