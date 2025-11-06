from openai import OpenAI

client = OpenAI(api_key="add your api key")

prompt = """You are a senior e-commerce market researcher with 7+ years of experience analyzing online retail categories (Amazon, Shopify, Wayfair, Etsy). You have strong skills in competitive analysis, unit economics, supplier sourcing, and digital advertising ROI. You write concise, data-focused reports for founders and growth teams.

Context:
The user plans to launch or scale an online furniture product in the US market in 2026. They want product ideas that sell well online, are simple to source/manufacture or dropship, fit typical e-commerce logistics, and can deliver high gross margins (>=40%) after landed cost and marketing. Focus on items suitable for direct-to-consumer and marketplace sales (not ultra-high-end bespoke pieces).

Task:
Perform market research to identify 5 furniture product ideas most likely to generate high online sales and strong profit margins. For each product idea, provide:

1. Product name and a one-line pitch.
2. Why it sells online — 3 succinct demand drivers (search trends, use-case, seasonality).
3. Estimated price range (retail) and target gross margin after COGS, shipping, and basic packaging.
4. Estimated landed cost / unit (manufacturing or wholesale) range and typical suppliers or regions.
5. Top sales channels (Amazon, Shopify DTC, Wayfair, Etsy, Facebook/IG) and recommended channel to launch.
6. Customer demographics & buyer intent.
7. Main competitors / example listings and one quick differentiator.
8. Difficulty score (1-5) for sourcing, fulfillment, and returns.
9. Recommended launch strategy & 3 quick growth tactics.
10. Key risks & mitigations.

Also produce:
- A summary Markdown table: Product | Retail Price | Est. Landed Cost | Est. Margin | Best Channel | Difficulty.
- Top 10 keywords to target for SEO/ads for the top product idea (short+long-tail).
- A 30-day go-to-market checklist for the chosen #1 product (supplier outreach, sample tests, listing copy, photo brief, ad budget, logistics setup).
- 90-day KPI table with measurable targets.

Formatting:
Return a structured Markdown document with headings for each product idea and the requested fields. Include the summary table, keywords list, 30-day checklist (numbered), and 90-day KPI table at the end.

Success criteria: actionable, realistic unit economics, and a prioritized launch plan for the #1 product.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system", "content":"You are a helpful assistant."},
        {"role":"user", "content": prompt}
    ],
    max_tokens=1500
)

print(response.choices[0].message.content)