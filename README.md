# estatpandas
estatpandas は、日本政府の公式統計ポータルである e-Stat からデータをダウンロードし、処理するための Python ライブラリです。このライブラリは、JSON 形式でデータを取得し、pandas DataFrame に変換して簡単に分析や操作ができるようにしています。  
  
`estatpandas` is a Python library that simplifies downloading and processing data from e-Stat, the Japanese government's official statistics portal. The library retrieves data in JSON format and converts it to a pandas DataFrame for easy analysis and manipulation.

## Installation

estatpandas を`pip`を使ってインストールすることができます: pip install estatpandas  
  
You can install this package using `pip`: pip install estatpandas

## Usage

```python
import estatpandas as epd

api_key = "your_api_key_here"
stats_data_id = "your_stats_data_id_here"

estat_df = epd.get_estat_dataframe(api_key, stats_data_id)
print(estat_df)
```

your_api_key_here を実際の e-Stat API キーに、your_stats_data_id_here を取得したいデータの ID に置き換えてください。  
  
Replace your_api_key_here with your actual e-Stat API key and your_stats_data_id_here with the ID of the data you want to retrieve.

## License
このプロジェクトは MIT ライセンスのもとでライセンスされています。  
  
This project is licensed under the MIT License.






