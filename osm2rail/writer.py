import csv
import os
from .utils import validate_download_dir

def saveNetwork(network, output_folder='csvfile', enconding=None):
    if output_folder:
        output_folder = validate_download_dir(output_folder)
        node_filepath = os.path.join(output_folder, 'node.csv')
        link_filepath = os.path.join(output_folder, 'link.csv')
        poi_filepath = os.path.join(output_folder, 'poi.csv')
    else:
        node_filepath = 'node.csv'
        link_filepath = 'link.csv'
        poi_filepath = 'poi.csv'

    try:
        if enconding is None:
            outfile = open(node_filepath, 'w', newline='', errors='ignore')
        else:
            outfile = open(node_filepath, 'w', newline='', errors='ignore', encoding=enconding)

        write = csv.writer(outfile)
        write.writerow(['name', 'node_id', 'osm_node_id', 'railway', 'level_crossing', 'access', 'description',
                        'x_coord', 'y_coord', 'geometry'])

        for node_id, node in network.node_dict.items():
            name = node.name if node.name else ''
            level_crossing = node.level_crossing if node.level_crossing else ''
            access = node.access if node.access else ''
            description = node.description if node.description else ''
            railway = node.railway if node.railway else ''
            geometry = node.geometry.wkt
            line = [name, node.node_id, node.osm_node_id, railway, level_crossing, access, description,
                    node.x_coord, node.y_coord, geometry]
            write.writerow(line)
        outfile.close()
    except PermissionError:
        print('node.csv may be locked by other programs. please release it then try again')

    try:
        if enconding is None:
            outfile = open(link_filepath, 'w', newline='', errors='ignore')
        else:
            outfile = open(link_filepath, 'w', newline='', errors='ignore', encoding=enconding)

        write = csv.writer(outfile)
        write.writerow(['name', 'link_id', 'osm_way_id', 'from_node_id', 'to_node_id', 'link_type_name', 'electrified',
                        'railway','frequency', 'highspeed', 'maxspeed','maxspeed_designed', 'passenger_lines', 'railway_ctcs',
                        'railway_traffic_mode', 'start_date','usage', 'voltage', 'gauge', 'service', 'length', 'geometry'])
        for link_id, link in network.link_dict.items():
            name = link.name if link.name else ''
            link_type_name = link.link_type_name if link.link_type_name else ''
            electrified = link.electrified if link.electrified else ''
            railway=link.railway if link.railway else ''
            frequency = link.frequency if link.frequency else ''
            highspeed = link.highspeed if link.highspeed else ''
            maxspeed = link.maxspeed if link.maxspeed else ''
            maxspeed_designed = link.maxspeed_designed if link.maxspeed_designed else ''
            passenger_lines = link.passenger_lines if link.passenger_lines else ''
            railway_ctcs = link.railway_ctcs if link.railway_ctcs else ''
            railway_traffic_mode = link.railway_traffic_mode if link.railway_traffic_mode else ''
            start_date = link.start_date if link.start_date else ''
            usage = link.usage if link.usage else ''
            voltage = link.voltage if link.voltage else ''
            gauge = link.gauge if link.gauge else ''
            service = link.service if link.service else ''
            line = [name, link.link_id, link.osm_way_id, link.from_node.node_id, link.to_node.node_id,
                    link_type_name, electrified, railway,frequency,highspeed, maxspeed, maxspeed_designed, passenger_lines,
                    railway_ctcs, railway_traffic_mode,start_date, usage, voltage, gauge, service, link.length,
                    link.geometry.wkt]
            write.writerow(line)
        outfile.close()
    except PermissionError:
        print('link.csv may be locked by other programs. please release it then try again')

    try:
        if len(network.POI_list):
            if enconding is None:
                outfile = open(poi_filepath, 'w', newline='', errors='ignore')
            else:
                outfile = open(poi_filepath, 'w', newline='', errors='ignore', encoding=enconding)

            write = csv.writer(outfile)
            write.writerow(['name', 'poi_id', 'osm_way_id', 'railway', 'geometry'])

            for poi in network.POI_list:
                name = ' ' + poi.name if poi.name else ''
                line = [name, poi.poi_id, poi.osm_way_id, poi.railway, poi.geometry.wkt]
                write.writerow(line)
            outfile.close()
    except PermissionError:
        print('poi.csv may be locked by other programs. please release it then try again')

