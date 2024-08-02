import json
import plotly.graph_objects as go
import plotly.io as pio

def load_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def process_data(data):
    clients = {}
    for session in data:
        if '/' in session['attendance']:  # Skip if attendance is in format 'x / y'
            continue
        client = session['attendance']
        if client not in clients:
            clients[client] = []
        clients[client].append({
            "type": session['type'],
            "time": session['time'],
            "day": session['day'],
            "staff": session['staff']
        })
    return clients

def prepare_plotly_table(clients):
    client_list = []
    service_list = []
    time_list = []
    day_list = []
    staff_list = []

    for client, services in clients.items():
        client_list.append(client)
        service_list.append(services[0]['type'])
        time_list.append(services[0]['time'])
        day_list.append(services[0]['day'])
        staff_list.append(", ".join(services[0]['staff']))
        for service in services[1:]:
            client_list.append("")
            service_list.append(service['type'])
            time_list.append(service['time'])
            day_list.append(service['day'])
            staff_list.append(", ".join(service['staff']))

    fig = go.Figure(data=[go.Table(
        header=dict(values=['Client', 'Service', 'Time', 'Day', 'Staff'],
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[client_list, service_list, time_list, day_list, staff_list],
                   fill_color='lavender',
                   align='left'))
    ])

    return fig

def main(file_path, output_file):
    data = load_data_from_file(file_path)
    clients = process_data(data)
    fig = prepare_plotly_table(clients)
    
    # Show the figure
    fig.show()

    # Save the figure as an HTML file
    pio.write_html(fig, output_file)
    print(f'Figure saved as {output_file}')

# Second param - output file
main('./data.json', 'normalized_data.html')
