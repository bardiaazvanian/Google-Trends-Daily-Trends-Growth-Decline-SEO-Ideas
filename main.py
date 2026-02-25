import json
from pytrends.request import TrendReq

keyword = "دانلود"

# hl رو روی fa می‌ذاریم تا نتایج فارسی رو بهتر تشخیص بده
pytrends = TrendReq(hl='hl', tz=210)

try:
    print(f"🔍 در حال ارتباط با گوگل برای بررسی ترندهای '{keyword}' (در ایران - ۷ روز گذشته)...")
    
    # اضافه کردن لوکیشن ایران (geo='IR') و تغییر بازه به ۷ روز (now 7-d)
    pytrends.build_payload([keyword], timeframe='now 7-d', geo='IR')
    related_dict = pytrends.related_queries()
    
    # استخراج هر دو لیستِ برتر (Top) و افزایشی (Rising)
    rising_df = related_dict[keyword].get('rising')
    top_df = related_dict[keyword].get('top')
    
    result = {"keyword": keyword, "top_trends": [], "rising_trends": []}
    
    # پردازش کلمات افزایشی (ترندهای داغ)
    if rising_df is not None and not rising_df.empty:
        result["rising_trends"] = rising_df.head(10).to_dict(orient='records')
        
    # پردازش کلمات پرسرچ (همیشه سبز)
    if top_df is not None and not top_df.empty:
        result["top_trends"] = top_df.head(10).to_dict(orient='records')

    print("\n✅ خروجی دیتای سئو:")
    print(json.dumps(result, indent=4, ensure_ascii=False))

except Exception as e:
    print(f"\n❌ ارور: {str(e)}")