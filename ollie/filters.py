import dash_core_components as dcc
import pandas as pd


def service_options():
    service_sql = """SELECT DISTINCT SERVICE_TYPE value FROM
    `bcx-insights.telkom_customerexperience.customerdata_20190902_00_anon`
    WHERE SERVICE_TYPE is not NULL AND CUSTOMER_NO_ANON in

    (SELECT DISTINCT ACCOUNT_NO_ANON FROM
    `bcx-insights.telkom_customerexperience.orders_20190903_00_anon`)"""

    options = pd.io.gbq.read_gbq(service_sql,
                                    project_id='bcx-insights',
                                    dialect='standard').fillna('N/A')

    options['label'] = options['value'].str.title()

    options = [{'label': x['label'],
                'value': x['value']} for _, x in options.iterrows()]

    return options


def customer_type():
    type_sql = """SELECT DISTINCT CUSTOMER_TYPE_DESC value FROM
    `bcx-insights.telkom_customerexperience.customerdata_20190902_00_anon`
    WHERE CUSTOMER_TYPE_DESC is not NULL AND CUSTOMER_NO_ANON in

    (SELECT DISTINCT ACCOUNT_NO_ANON FROM
    `bcx-insights.telkom_customerexperience.orders_20190903_00_anon`)"""

    types = pd.io.gbq.read_gbq(type_sql,
                                    project_id='bcx-insights',
                                    dialect='standard').fillna('N/A')

    types['label'] = types['value'].str.title()

    types = [{'label': x['label'],
                'value': x['value']} for _, x in types.iterrows()]

    return types

if __name__ == '__main__':
    print(service_options())
