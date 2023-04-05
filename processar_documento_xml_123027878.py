# Trabalho 1 - Caroline da Conceição Lima - DRE: 123027878 - Mestranda EDC
# Data de entrega: 06/04/2023
# Para provar que aprendeu XML você deve fazer uma pequena atividade.
# Baixe a nossa Base Oficial de Trabalho (CysticFibrosis2)
# Escolha dois processadores de XML diferentes em Python, A e B (DOM, SAX ou outro)
# Use um processador A para obter o nome de todos os AUTHOR citados no arquivo cf79.xml, salve 1 por linha no arquivo autores.xml
# Use um processador B para obter o nome de todos os TITLE citados no arquivo cf79.xml, salve 1 por linha no arquivo titulo.xml

# Processador A para obter os autores - AUTHOR(TAG), author(atributo): DOM
import xml.dom.minidom as MD

# Processador B para obter os títulos - Tag TITLE: ElementTree
import xml.etree.ElementTree as ET

# Criando o documento através do DOM
root_DOM = MD.Document()
element = root_DOM.createElement('author')
root_DOM.appendChild(element)

# Abrindo arquivo "cf79.xml"
with open("cf79.xml", 'r', encoding='utf-8') as file:
    # Parse pelo Dom
    xml_DOM = MD.parse(file)

    # Obtento atributo author da TAG CITE
    cites = xml_DOM.getElementsByTagName("CITE")

    for cite in cites:
        cite_author = cite.getAttribute('author');
        # Salvando o nome do atributo author no documento
        author_child = root_DOM.createElement('author')
        author_child.setAttribute('name', cite_author)
        element.appendChild(author_child)

    # Obtendo TAG AUTHOR
    authors = xml_DOM.getElementsByTagName("AUTHOR")

    for authors_name in authors:
        # Salvando o nome da TAG author no documento
        author_child = root_DOM.createElement('author')
        author_child.setAttribute('name', authors_name.firstChild.data)
        element.appendChild(author_child)

    # Inserindo Indentação
    xml_str_DOM = root_DOM.toprettyxml(indent="\t")

    # Salvando listagem em autores.xml
    path_file = "autores.xml"
    with open(path_file, 'w') as result_file_dom:
        result_file_dom.write(xml_str_DOM)

    # Parse pelo ElementTree
    xml_ET = ET.parse("cf79.xml")
    root_ET = xml_ET.getroot()

    titles = root_ET.findall(".//TITLE")

    result_root = ET.Element("TITLE_LIST")

    for title in titles:
        result_root.append(title)

    tree = ET.ElementTree(result_root)
    tree.write("titulos.xml", encoding='utf-8', xml_declaration=True)