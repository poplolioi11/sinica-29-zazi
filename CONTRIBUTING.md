# 回報與修正

請在Issue或Pull Request提供：所用Git提交或SHA-256、畫布與fol.標籤、region/line id、原讀及擬改字、官方原圖URL、可見筆畫或缺損的理由。不要以通行文本或模型一致取代影像證據。候選未能定讀時保留□並修改疑字紀錄；不將後出不同刊本的文字無記錄補入。

修改 `sinica-29.json` 時，同步更新相關review、`corrections.json`與`uncertainties.json`及coverage計數，執行 `python3 export_txt.py` 匯出TXT，重算SHA256SUMS，再執行 `python3 verify.py`。重新核圖者應寫明實際核對範圍、日期與AI／人工角色，不把局部修正標成全書人工校勘。

不提交掃描圖、裁圖、第三方OCR正文、私人信箱或真實姓名。原文自由重用不以回報、署名或告知維護者為條件；若引用受CC BY 4.0保護的新寫說明，依LICENSE.md標示來源。
