{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "80e775b5-6324-4649-babf-6f8a8aa2b465",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "                            Some older sites might still use frames to break up thier pages. Modern ones might be using iFrames to expose data. Learn about turtles as you scrape content inside frames.\n",
      "                            See if you can find the 'real' URL that our content is being loaded from, and scrape that page. Also practice interating over a list of items and loading their detail pages to get more information about each one.\n",
      "                        \n",
      "\n",
      " There are 3 video lessons that show you how to scrape this page.\n",
      "                        \n",
      "\n",
      "                            \n",
      "                                Data via\n",
      "                                https://en.wikipedia.org/wiki/List_of_Testudines_families\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "url='https://www.scrapethissite.com/pages/frames/'\n",
    "response=requests.get(url)\n",
    "if response.status_code==200:\n",
    "    soup=BeautifulSoup(response.content,'html.parser')\n",
    "    paragraphs=soup.find_all('p')\n",
    "    for p in paragraphs:\n",
    "        print(p.get_text())\n",
    "else:\n",
    "    print(f\"failed to retrive webpage.Status_code:{response.status_code}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dda6ded2-9efa-4db4-bbe7-fcfcfe25fb43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data saved to countries_simple.xlsx\n",
      "                Country           Capital Population      Area\n",
      "0               Andorra  Andorra la Vella      84000     468.0\n",
      "1  United Arab Emirates         Abu Dhabi    4975593   82880.0\n",
      "2           Afghanistan             Kabul   29121286  647500.0\n",
      "3   Antigua and Barbuda        St. John's      86754     443.0\n",
      "4              Anguilla        The Valley      13254     102.0\n",
      "Total countries: 250\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "\n",
    "def scrape_simple_countries():\n",
    "    url = \"https://www.scrapethissite.com/pages/simple/\"\n",
    "    headers = {\"User-Agent\": \"Mozilla/5.0\"}\n",
    "    resp = requests.get(url, headers=headers)\n",
    "    resp.raise_for_status()\n",
    "    soup = BeautifulSoup(resp.text, \"html.parser\")\n",
    "\n",
    "    country_divs = soup.find_all(\"div\", class_=\"col-md-4 country\")\n",
    "\n",
    "    data = []\n",
    "    for c in country_divs:\n",
    "        name_tag = c.find(\"h3\", class_=\"country-name\")\n",
    "        name = name_tag.get_text(strip=True) if name_tag else \"\"\n",
    "        info = c.find(\"div\", class_=\"country-info\")\n",
    "        if info:\n",
    "            cap = info.find(\"span\", class_=\"country-capital\")\n",
    "            population = info.find(\"span\", class_=\"country-population\")\n",
    "            area = info.find(\"span\", class_=\"country-area\")\n",
    "\n",
    "            capital = cap.get_text(strip=True) if cap else \"\"\n",
    "            pop = population.get_text(strip=True) if population else \"\"\n",
    "            area_km = area.get_text(strip=True) if area else \"\"\n",
    "        else:\n",
    "            capital = pop = area_km = \"\"\n",
    "\n",
    "        data.append([name, capital, pop, area_km])\n",
    "\n",
    "    # Create DataFrame\n",
    "    df = pd.DataFrame(data, columns=[\"Country\", \"Capital\", \"Population\", \"Area\"])\n",
    "\n",
    "    return df\n",
    "\n",
    "def main():\n",
    "    df = scrape_simple_countries()\n",
    "    if df.empty:\n",
    "        print(\"No data scraped. Check your selectors or if the site changed.\")\n",
    "        return\n",
    "\n",
    "    excel_file = \"countries_simple.xlsx\"\n",
    "    df.to_excel(excel_file, index=False)\n",
    "\n",
    "    print(f\"Data saved to {excel_file}\")\n",
    "    print(df.head())\n",
    "    print(f\"Total countries: {len(df)}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40c93cd2-8c2e-41bf-9ca2-f278621c0c3f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
