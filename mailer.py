import requests


def send_mail(api_key, domain_name):
    return requests.post(
        f"https://api.mailgun.net/v3/{domain_name}/messages",
        auth=("api", api_key),
        data={
            f"from": "Excited User <postmaster@{domain_name}>",
            "to": ["eitan.simler@gmail.com", ],
            "subject": "Hello",
            "text": "Testing some Mailgun awesomness!"
        })


def main():
    API_KEY = '2366aee1194ef7806e44a69ea9e7e882-f8b3d330-b60449f3'
    DOMAIN_NAME = 'sandbox58a468e43fc8409580540c0cbfbd6678.mailgun.org'

    print(send_mail(API_KEY, DOMAIN_NAME))


if __name__ == '__main__':
    main()
