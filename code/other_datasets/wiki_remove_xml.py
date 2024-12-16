import xml.etree.ElementTree as ET
import re

# Path to your large XML file
xml_file = '/home/delve/kaggle/enwiki-20240801-pages-meta-current.xml'

output_file = open('/home/delve/kaggle/wiki.txt', "w")

def extract_text_from_xml(xml_file):
    context = ET.iterparse(xml_file, events=('end',))
    ref_math_pattern = re.compile(r'<ref[^>]*>.*?</ref>|<math[^>]*>.*?</math>', re.DOTALL)

    for event, elem in context:
        if elem.tag.endswith('text'):  # Handles namespaced tags
            if elem.text:
                cleaned_text = re.sub(ref_math_pattern, '', elem.text)
                output_file.write(cleaned_text)  # Process the text content as needed
        elem.clear()  # Free memory

extract_text_from_xml(xml_file)

