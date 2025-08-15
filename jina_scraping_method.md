# Jina Scraping Method

## Command Structure
```bash
curl "https://r.jina.ai/[TARGET_URL]" \
  -H "Authorization: Bearer jina_2aa5fe1199e447778cd48f6bebf89d0fnwWivQYYoNzvrN8itDVlpRi9woUk"
```

## Important Notes
- If a page 404s or doesn't scrape properly, scrape it again
- Do NOT use Jina to scrape CSS of design sites
- Store all SEPARATE pages in `/research/[technology]/page1/2/3/4/5/6/7/8` etc. directories with individual .md files
- Create llm.txt files from successful scrapes for easy reference