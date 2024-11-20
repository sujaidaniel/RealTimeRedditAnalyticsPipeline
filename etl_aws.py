import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY

def connect_to_s3():
    """Establishes a connection to Amazon S3 using provided credentials."""
    try:
        return s3fs.S3FileSystem(anon=False, key=AWS_ACCESS_KEY_ID, secret=AWS_ACCESS_KEY)
    except Exception as error:
        print(f"Error connecting to S3: {error}")

def ensure_bucket_exists(s3: s3fs.S3FileSystem, bucket_name: str):
    """Creates the specified S3 bucket if it doesn't already exist."""
    try:
        if not s3.exists(bucket_name):
            s3.mkdir(bucket_name)
            print("Bucket created successfully.")
        else:
            print("Bucket already exists.")
    except Exception as error:
        print(f"Error ensuring bucket exists: {error}")

def upload_file_to_s3(s3: s3fs.S3FileSystem, local_file_path: str, bucket_name: str, s3_file_name: str):
    """Uploads a file to the specified S3 bucket."""
    try:
        s3.put(local_file_path, f"{bucket_name}/raw/{s3_file_name}")
        print("File successfully uploaded to S3.")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as error:
        print(f"Error uploading file to S3: {error}")
