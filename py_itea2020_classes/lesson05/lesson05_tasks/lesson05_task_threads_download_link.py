from threading import Thread
import wget


def new_thread_decorator(thread_name, thread_is_daemon):
    def actual_decorator(func):

        def wrapper(link, target_folder=r'C:\my_python\python_itea2020\py_itea2020_classes\lesson05\lesson05_tasks'):
            t1 = Thread(target=func, args=(link, target_folder), name=thread_name, daemon=thread_is_daemon)
            t1.start()

        return wrapper

    return actual_decorator


@new_thread_decorator('Thread A', False)
def download_file(link, target_folder=r'C:\my_python\python_itea2020\py_itea2020_classes\lesson05\lesson05_tasks'):
    print(f'Starting to download file from {link}')
    wget.download(link, target_folder)
    print(f'Finished downloading file from {link}')


links_list = ['https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2019'
              '-financial-year-provisional/Download-data/annual-enterprise-survey-2019-financial-year-provisional'
              '-size-bands-csv.csv',
              'https://www.stats.govt.nz/assets/Uploads/Business-price-indexes/Business-price-indexes-June-2020'
              '-quarter/Download-data/business-price-indexes-june-2020-quarter-corrections-to-previously-published'
              '-statistics.csv',
              'https://www.stats.govt.nz/assets/Uploads/Business-operations-survey/Business-operations-survey-2019'
              '/Download-data/business-operations-survey-2019-international-engagement-csv.csv',
              'https://www.stats.govt.nz/assets/Uploads/Electronic-card-transactions/Electronic-card-transactions'
              '-October-2020/Download-data/electronic-card-transactions-october-2020-csv-tables.zip',
              'https://www.stats.govt.nz/assets/Uploads/Annual-balance-sheets/Annual-balance-sheets-2017-provisional'
              '/Download-data/annual-balance-sheets-and-accumulation-accounts-200817-provisional-csv.csv',
              'https://www.stats.govt.nz/assets/Uploads/Balance-of-payments/Balance-of-payments-and-international'
              '-investment-position-June-2020-quarter/Download-data/balance-of-payments-international-investment'
              '-position-jun20-csv-tables.zip',
              'https://www.stats.govt.nz/assets/Uploads/Household-living-costs-price-indexes/Household-living-costs'
              '-price-indexes-September-2020-quarter/Download-data/Household-living-costs-price-indexes-September'
              '-2020-quarter-expenditure-weights-CSV.csv',
              'https://www.stats.govt.nz/assets/Uploads/National-accounts-changes-in-assets/National-accounts-changes'
              '-in-assets-2008-16/Download-data/national-accounts-change-assets-accumulation-accounts-2008-16'
              '-provisional.csv',
              'https://www.stats.govt.nz/assets/Uploads/Regional-gross-domestic-product/Regional-gross-domestic'
              '-product-Year-ended-March-2019/Download-data/regional-gross-domestic-product-year-ended-march-2019.csv',
              'https://www.stats.govt.nz/assets/Uploads/Local-authority-financial-statistics/Local-authority'
              '-financial-statistics-Year-ended-June-2019-Infoshare-tables/Download-data/local-authority-financial'
              '-statistics-year-ended-june-2019-csv.zip']

for lnk in links_list:
    download_file(lnk)