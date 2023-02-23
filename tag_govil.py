# Imports
import requests
import json

# Constants
RESOURCE_ID = "c8b9f9c8-4612-4068-934f-d4acd2e3c06e"
LIMIT = 600000
RESULT_FILE_NAME = "data.json"

choice = int(input("""
\t1 - Search by car number
\t2 - Pull everything

Enter your choice: """))


def parse_response(response):
    content = response.content.decode('utf-8')
    return json.loads(content)['result']['records']


def main():
    if choice == 1:
        car_number = input("Enter your car number: ")
        url = f'https://data.gov.il/api/3/action/datastore_search?resource_id={RESOURCE_ID}&q={car_number}'
        results = parse_response(requests.get(url))
        for result in results:
            print(result)
    elif choice == 2:
        print("[+] Pulling all the data")
        url = f'https://data.gov.il/api/3/action/datastore_search?resource_id={RESOURCE_ID}&limit={LIMIT}'
        print("[+] Done pulling")
        results = parse_response(requests.get(url))
        print(f"[+] Saving the data to {RESULT_FILE_NAME}")
        with open(RESULT_FILE_NAME, 'w') as f:
            json.dump(results, f, sort_keys=True, indent=4)


if __name__ == "__main__":
    main()
