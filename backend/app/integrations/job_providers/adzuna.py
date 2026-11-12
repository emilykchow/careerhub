import httpx

# Per minute. Up to 25 calls.
# Per day. Up to 250 calls.
# Per week. Up to 1,000 calls.
# Per month. Up to 2,500 calls.


async def get_jobs():
    url = f"http://api.adzuna.com:80/v1/api/jobs/gb/search/1?app_id={YOUR_APP_ID}&app_key={YOUR_APP_KEY}&results_per_page=20&what=javascript%20developer&what_exclude=java&where=london&sort_by=salary&salary_min=30000&full_time=1&permanent=1&content-type=application/json"

    payload = {}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, payload)
        print(f"response {response}")
