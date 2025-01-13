import csv
import xml.dom.minidom
import xml.etree.ElementTree as ET

def create_xml():
    # Create the root element
    root = ET.Element("atletas")
    
    # Read CSV file
    with open('atletas.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        # Process each row
        for row in csvreader:
            # Create athlete element
            atleta = ET.SubElement(root, "atleta")
            
            # Add child elements for each field
            nome = ET.SubElement(atleta, "nome")
            nome.text = row['nome']
            
            apelido = ET.SubElement(atleta, "apelido")
            apelido.text = row['apelido']
            
            data_nascimento = ET.SubElement(atleta, "data_nascimento")
            data_nascimento.text = row['data_nascimento']
            
            posicao = ET.SubElement(atleta, "posicao")
            posicao.text = row['posicao']
            
            mao = ET.SubElement(atleta, "mao")
            mao.text = row['mao']
    
    # Create XML string with proper formatting
    xmlstr = xml.dom.minidom.parseString(ET.tostring(root, encoding='unicode')).toprettyxml(indent="  ")
    
    # Write to file
    with open('atletas.xml', 'w', encoding='utf-8') as f:
        f.write(xmlstr)

if __name__ == "__main__":
    create_xml()
