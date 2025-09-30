import subprocess

try:
    subprocess.run(["python", "scripts/ingest.py"], check=True)
    print("Ingestion complete")
except subprocess.CalledProcessError as e:
    print(f"Ingestion failed: {e}")
    exit(1)

try:
    subprocess.run(["python", "scripts/transform.py"], check=True)
    print("Transformation complete")
except subprocess.CalledProcessError as e:
    print(f"Transformation failed: {e}")
    exit(1)