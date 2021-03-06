# encoding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from asgard.conf import settings
from asgard.models.user import UserDB as User
from asgard.models.user_has_account import UserHasAccount
from hollowman.conf import HOLLOWMAN_DB_ECHO

engine = create_engine(settings.DB_URL, echo=HOLLOWMAN_DB_ECHO)
HollowmanSession = sessionmaker(bind=engine)
