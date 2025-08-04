from tinydb import TinyDB, Query
from src.analyser.models.job import Job
from src.analyser.models.resum import Resum
from src.analyser.models.analysis import Analysis
from src.analyser.models.file import File

class AnalyserDatabase(TinyDB):
    def __init__(self, file_path='db.json'):
        super().__init__(file_path)
        self.jobs = self.table("jobs")
        self.resums = self.table("resums")
        self.analysis = self.table("analysis")
        self.files = self.table("files")

    # JOB CRUD
    def insert_job(self, job: Job):
        self.jobs.insert(job.model_dump())

    def get_job_by_name(self, name: str):
        query = Query()
        result = self.jobs.search(query.name == name)
        return result[0] if result else None

    def update_job(self, new_data: Job):
        query = Query()
        self.jobs.update(new_data.model_dump(), query.id == new_data.id)

    def delete_job_by_id(self, job_id: str):
        query = Query()
        self.jobs.remove(query.id == job_id)

    # RESUM CRUD
    def insert_resum(self, resum: Resum):
        self.resums.insert(resum.model_dump())

    def get_resums_by_job_id(self, job_id: str):
        query = Query()
        return self.resums.search(query.job_id == job_id)

    # ANALYSIS CRUD
    def insert_analysis(self, analysis: Analysis):
        self.analysis.insert(analysis.model_dump())

    def get_analysis_by_job_id(self, job_id: str):
        query = Query()
        return self.analysis.search(query.job_id == job_id)

    # FILES CRUD
    def insert_file(self, file: File):
        self.files.insert(file.model_dump())

    def get_last_file_by_job_id(self, job_id: str):
        query = Query()
        results = self.files.search(query.job_id == job_id)
        return results[-1] if results else None
