import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer

# class SearchJobsView(APIView):
#     def get(self, request, query):
#         upwork_jobs = self.search_upwork(query)
#         kwork_jobs = self.search_kwork(query)
#         all_jobs = upwork_jobs + kwork_jobs
#         serializer = JobSerializer(all_jobs, many=True)
#         return Response(serializer.data)
#
#     def search_upwork(self, query):
#         url = f"https://www.upwork.com/nx/search/jobs?q={query}"
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")
#         jobs = []
#         for job_card in soup.select(".card-list-container"):
#             title = job_card.select_one(".job-tile").text.strip()
#             url = "https://www.upwork.com" + job_card.select_one(".job-tile-header")["href"]
#             job = Job(title=title, url=url, platform="Upwork")
#             jobs.append(job)
#         return jobs
#
#     def search_kwork(self, query):
#         url = f"https://kwork.ru/search?query={query}"
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")
#         jobs = []
#         for job_card in soup.select(".wants-kwork"):
#             title = job_card.select_one(".wants-kwork__header").text.strip()
#             url = "https://kwork.ru" + job_card.select_one(".wants-kwork__header a")["href"]
#             job = Job(title=title, url=url, platform="Kwork")
#             jobs.append(job)
#         return jobs
