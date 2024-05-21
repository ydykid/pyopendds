import sys
from datetime import timedelta

from pyopendds import (
    opendds_version_dict,
    init_opendds,
    DomainParticipant,
    StatusKind,
    PyOpenDDS_Error,
)
from pybasic.basic import Reading

if __name__ == "__main__":
    print('123')
    print('OpenDDS Version is:', opendds_version_dict())
    try:
        print('Publisher:')
        # Initialize OpenDDS and Create DDS Entities
        init_opendds(opendds_debug_level=1)
        domain = DomainParticipant(34)
        topic = domain.create_topic('Readings', Reading)
        publisher = domain.create_publisher()
        print('publisher:', publisher)
        qos = publisher.get_default_datawriter_qos()
        print('qos:', qos)
        writer = publisher.create_datawriter(topic)
        # writer.
        print('writer:', writer)

        # Wait for Publisher to Connect
        # print('Waiting for Publisher...')
        # reader.wait_for(StatusKind.SUBSCRIPTION_MATCHED, timedelta(seconds=5))
        # print('Found Publisher!...123')

        # Read and Print Sample
        # print(reader.take_next_sample())

        print('Done!')

    except PyOpenDDS_Error as e:
        print('PyOpenDDS_Error:', e)
        sys.exit(e)
