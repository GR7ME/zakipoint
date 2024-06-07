from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()


def generate_logs(log_type, count=10):
    logs = []
    statuses = ["WARN", "ERROR", "INFO", "UPDATE"]
    start_date = datetime(2023, 1, 23, 0, 27, 35, 41218)  # Start timestamp
    end_date = datetime(2024, 6, 6, 1, 20, 50, 235178)
    for _ in range(count):
        log_entry = {
            "TIMESTAMP": fake.date_time_between(
                start_date=start_date, end_date=end_date
            ).isoformat(),
            "MESSAGE STATUS": random.choice(statuses),
            "MESSAGE": fake.sentence(),
        }
        logs.append(log_entry)
    return logs


def generate_pyspark_log():
    log_group = {
        "LOG GROUP": {
            "PYSPARK": {
                "PYSPARK 1": {"LOGS": generate_logs("PYSPARK", 30)},
                "PYSPARK 2": {"LOGS": generate_logs("PYSPARK", 10)},
            },
            "Elasticsearch": {
                "Elasticsearch1": {"LOGS": generate_logs("Elasticsearch", 10)},
                "Elasticsearch2": {"LOGS": generate_logs("Elasticsearch", 20)},
            },
            "Pentaho": {
                "Pentaho1": {"LOGS": generate_logs("Pentaho", 5)},
                "Pentaho2": {"LOGS": generate_logs("Pentaho", 5)},
            },
        },
        "1": generate_logs("Elasticsearch", 500),
        "2": generate_logs("Pyspark", 300),
        "3": generate_logs("Pentaho", 200),
    }
    return log_group
