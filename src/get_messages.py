from utils import get_env
from dotenv.main import load_dotenv
from melipayamak import Api
import datetime

load_dotenv()

FROM = get_env("FROM")
date_from = datetime.datetime(2020, 5, 17).date()
date_to = datetime.datetime(2020, 5, 17).date()
username = "09126008461"
password = "LE5F3"
location = 1
index = 1
count = 20


api = Api(username, password)
sms = api.sms("soap")
messages = sms.get_messages_by_date(
    location=location,
    index=index,
    count=count,
    _from=FROM,
    dateFrom=date_from,
    dateTo=date_to,
)

print(messages)
# for message in messages:
#     print(message)
