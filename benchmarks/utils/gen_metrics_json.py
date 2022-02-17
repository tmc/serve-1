import argparse
import csv
import json

def extract_metrics(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        for row in csv_reader:
            model = row["Model"]
            index = model.rfind('/') + 1
            row["Model"] = model[index:-4]
            return row

    return None

def gen_metrics_json(csv_dict):
    if csv_dict is None:
        return

    metrics_dict_list = []
    for k, v in csv_dict.items():
        if k == "TS throughput":
            metrics_dict_list.append({
                "MetricName" : '{}_{}'.
                    format(csv_dict["Model"], "throughput"),
                "Dimensions": [
                    {"Name": "batch_size", "Value": csv_dict["Batch size"]}
                ],
                "Unit": 'Count/Second',
                "Value": float(v)})
        elif k == "TS latency P50":
            metrics_dict_list.append({
                "MetricName": '{}_{}'.
                    format(csv_dict["Model"], "total_latency_P50"),
                "Dimensions": [
                    {"Name": "batch_size", "Value": csv_dict["Batch size"]}
                ],
                "Unit": 'Milliseconds',
                "Value": float(v)})
        elif k == "TS latency P90":
            metrics_dict_list.append({
                "MetricName": '{}_{}'.
                    format(csv_dict["Model"], "total_latency_P90"),
                "Dimensions": [
                    {"Name": "batch_size", "Value": csv_dict["Batch size"]}
                ],
                "Unit": 'Milliseconds',
                "Value": float(v)})
        elif k == "TS latency P99":
            metrics_dict_list.append({
                "MetricName": '{}_{}'.
                    format(csv_dict["Model"], "total_latency_P99"),
                "Dimensions": [
                    {"Name": "batch_size", "Value": csv_dict["Batch size"]}
                ],
                "Unit": 'Milliseconds',
                "Value": float(v)})
        elif k == "Model_p50":
            metrics_dict_list.append({
                "MetricName": '{}_{}'.
                    format(csv_dict["Model"], "model_latency_P50"),
                "Dimensions": [
                    {"Name": "batch_size", "Value": csv_dict["Batch size"]}
                ],
                "Unit": 'Milliseconds',
                "Value": float(v)})
        elif k == "Model_p90":
            metrics_dict_list.append({
                "MetricName": '{}_{}'.
                    format(csv_dict["Model"], "model_latency_P90"),
                "Dimensions": [
                    {"Name": "batch_size", "Value": csv_dict["Batch size"]}
                ],
                "Unit": 'Milliseconds',
                "Value": float(v)})
        elif k == "Model_p99":
            metrics_dict_list.append({
                "MetricName": '{}_{}'.
                    format(csv_dict["Model"], "model_latency_P99"),
                "Dimensions": [
                    {"Name": "batch_size", "Value": csv_dict["Batch size"]}
                ],
                "Unit": 'Milliseconds',
                "Value": float(v)})

    print(json.dumps(metrics_dict_list, indent = 4))

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        action="store",
        help="ab report csv file path",
    )

    arguments = parser.parse_args()
    csv_dict = extract_metrics(arguments.input)
    gen_metrics_json(csv_dict)

if __name__ == "__main__":
    main()







