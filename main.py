import requests


def get(page):
    response = None
    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
    }
    url = f"https://reqres.in/api/users?page={page}"
    try:
        with requests.Session() as session:
            session.headers.update(h)
            response = session.get(url=url, headers=h)
            response.raise_for_status()
    except Exception as exception:
        print(exception)
    return response

def get_user_full_name(start, end):
    result = []
    if not isinstance(start, int) or not isinstance(end, int):
        return result
    for page in range(1, 3):
        resp = get(page)
        if resp is None:
            break
        for data in resp.json()["data"]:
            iid = data["id"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            if start <= iid <= end:
                result.append(f"{first_name} {last_name}")
    return sorted(result)


if __name__ == "__main__":
    result1 = get_user_full_name(1, 3)
    print(result1)
    assert result1 == ['Emma Wong', 'George Bluth', 'Janet Weaver']

    result2 = get_user_full_name(5, 8)
    print(result2)
    assert result2 == ['Charles Morris', 'Lindsay Ferguson', 'Michael Lawson', 'Tracey Ramos']

    result3 = get_user_full_name("1", 10)
    print(result3)
    assert result3 == []

    result4 = get_user_full_name(1, "10")
    print(result4)
    assert result4 == []

    result5 = get_user_full_name(-2, -1)
    print(result5)
    assert result5 == []

    result6 = get_user_full_name(0, 1)
    print(result6)
    assert result6 == ['George Bluth']

    result7 = get_user_full_name(0, 0)
    print(result7)
    assert result7 == []

    result8 = get_user_full_name(13, 20)
    print(result8)
    assert result8 == []

    result9 = get_user_full_name(1, 12)
    print(result9)
    assert result9 == ['Byron Fields', 'Charles Morris', 'Emma Wong', 'Eve Holt', 'George Bluth', 'George Edwards', 'Janet Weaver', 'Lindsay Ferguson', 'Michael Lawson', 'Rachel Howell', 'Tobias Funke', 'Tracey Ramos']