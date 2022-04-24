import panel
from connector import connetSql
cursor, sqlConnect = connetSql('7640_proj')
# user_id, user_name = customer_operation.log_in(sqlConnect, cursor)
user_name = ''
user_id = 0

def main():
    panel.showLandingPage(user_name)


if __name__ == '__main__':
    main()

