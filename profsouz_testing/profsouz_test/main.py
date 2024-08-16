import pandas
from playwright.sync_api import Playwright, sync_playwright, expect


def parse_python_versions(playwright: Playwright):
    data = []

    with playwright.chromium.launch(headless=True) as browser:
        with browser.new_context() as context:
            with context.new_page() as page:
                page.goto("https://www.python.org/downloads/")
                table = page.locator("div.download-list-widget li").all()
                for string in table:
                    string_data = {
                        "Release version": string.locator('span.release-number a').text_content(),
                        "Release date": string.locator('span.release-date').text_content(),
                        "Download": string.locator('span.release-download a').get_attribute('href'),
                        "Release Notes": string.locator('span.release-enhancements a').get_attribute('href')
                    }
                    data.append(string_data)
                page.close()
    return data


def write_to_exel(data):
    data = pandas.DataFrame(data)
    print(data)
    data.to_excel('Python releases by version number.xlsx', index=False)


with sync_playwright() as playwright:
    write_to_exel(parse_python_versions(playwright))
