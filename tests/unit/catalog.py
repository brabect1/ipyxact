import unittest
import io
import os
import sys
import xml.etree.ElementTree as ET

import ipyxact.ipyxact

sys.path.append(os.path.dirname(__file__))
from XmlUtils import xml_compare

data = {
    # example from https://github.com/kactus2/ipxactexamplelib: tut.fi/examples/MemoryDesign/1.0/MemoryDesign.1.0.xml
    'kactus2-MemoryDesign': '''<?xml version="1.0" encoding="UTF-8"?>
<ipxact:catalog xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ipxact="http://www.accellera.org/XMLSchema/IPXACT/1685-2014" xmlns:kactus2="http://kactus2.cs.tut.fi" xsi:schemaLocation="http://www.accellera.org/XMLSchema/IPXACT/1685-2014/ http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd">
	<ipxact:vendor>tut.fi</ipxact:vendor>
	<ipxact:library>examples</ipxact:library>
	<ipxact:name>MemoryDesign</ipxact:name>
	<ipxact:version>1.0</ipxact:version>
	<ipxact:description>This catalog contains all the IP-XACT files used in th eMemory Design video tutorial for Kactus2.</ipxact:description>
	<ipxact:catalogs>
		<ipxact:ipxactFile>
			<ipxact:vlnv vendor="tut.fi" library="cpu.structure" name="cpu_example.documents" version="1.0"/>
			<ipxact:name>../../../cpu.structure/cpu_example.documents/1.0/cpu_example.documents.1.0.xml</ipxact:name>
		</ipxact:ipxactFile>
	</ipxact:catalogs>
	<ipxact:vendorExtensions>
		<kactus2:version>3,4,108,0</kactus2:version>
	</ipxact:vendorExtensions>
</ipxact:catalog>''',
# example from https://github.com/kactus2/ipxactexamplelib: tut.fi/other.subsystem/spi_example.documents/1.0/spi_example.documents.1.0.xml
'kactus2-spi_example': '''<?xml version="1.0" encoding="UTF-8"?>
<ipxact:catalog xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ipxact="http://www.accellera.org/XMLSchema/IPXACT/1685-2014" xmlns:kactus2="http://kactus2.cs.tut.fi" xsi:schemaLocation="http://www.accellera.org/XMLSchema/IPXACT/1685-2014/ http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd">
	<ipxact:vendor>tut.fi</ipxact:vendor>
	<ipxact:library>other.subsystem</ipxact:library>
	<ipxact:name>spi_example.documents</ipxact:name>
	<ipxact:version>1.0</ipxact:version>
	<ipxact:description>List of IP-XACT documents in the SPI example.The top-level component is tut.fi:other.subsystem:spi_example:1.0.</ipxact:description>
	<ipxact:busDefinitions>
		<ipxact:ipxactFile>
			<ipxact:vlnv vendor="tut.fi" library="interface" name="spi" version="1.0"/>
			<ipxact:name>../../../interface/spi/1.0/spi.1.0.xml</ipxact:name>
		</ipxact:ipxactFile>
	</ipxact:busDefinitions>
	<ipxact:abstractionDefinitions>
		<ipxact:ipxactFile>
			<ipxact:vlnv vendor="tut.fi" library="interface" name="spi.absDef" version="1.0"/>
			<ipxact:name>../../../interface/spi/1.0/spi.absDef.1.0.xml</ipxact:name>
		</ipxact:ipxactFile>
	</ipxact:abstractionDefinitions>
	<ipxact:components>
		<ipxact:ipxactFile>
			<ipxact:vlnv vendor="tut.fi" library="communication.template" name="spi_master" version="1.0"/>
			<ipxact:name>../../../communication.template/spi_master/1.0/spi_master.1.0.xml</ipxact:name>
		</ipxact:ipxactFile>
		<ipxact:ipxactFile>
			<ipxact:vlnv vendor="tut.fi" library="communication.template" name="spi_slave" version="1.0"/>
			<ipxact:name>../../../communication.template/spi_slave/1.0/spi_slave.1.0.xml</ipxact:name>
		</ipxact:ipxactFile>
		<ipxact:ipxactFile>
			<ipxact:vlnv vendor="tut.fi" library="other.subsystem" name="spi_example" version="1.0"/>
			<ipxact:name>../../../other.subsystem/spi_example/1.0/spi_example.1.0.xml</ipxact:name>
		</ipxact:ipxactFile>
	</ipxact:components>
	<ipxact:designs>
		<ipxact:ipxactFile>
			<ipxact:vlnv vendor="tut.fi" library="other.subsystem" name="spi_example.design" version="1.0_adhoc"/>
			<ipxact:name>../../../other.subsystem/spi_example/1.0/spi_example.design.1.0_adhoc.xml</ipxact:name>
		</ipxact:ipxactFile>
		<ipxact:ipxactFile>
			<ipxact:vlnv vendor="tut.fi" library="other.subsystem" name="spi_example.design" version="1.0_bus"/>
			<ipxact:name>../../../other.subsystem/spi_example/1.0/spi_example.design.1.0_bus.xml</ipxact:name>
		</ipxact:ipxactFile>
	</ipxact:designs>
	<ipxact:designConfigurations>
		<ipxact:ipxactFile>
			<ipxact:vlnv vendor="tut.fi" library="other.subsystem" name="spi_example.designcfg" version="1.0_adhoc"/>
			<ipxact:name>../../../other.subsystem/spi_example/1.0/spi_example.designcfg.1.0_adhoc.xml</ipxact:name>
		</ipxact:ipxactFile>
		<ipxact:ipxactFile>
			<ipxact:vlnv vendor="tut.fi" library="other.subsystem" name="spi_example.designcfg" version="1.0_bus"/>
			<ipxact:name>../../../other.subsystem/spi_example/1.0/spi_example.designcfg.1.0_bus.xml</ipxact:name>
		</ipxact:ipxactFile>
	</ipxact:designConfigurations>
	<ipxact:vendorExtensions>
		<kactus2:version>3,3,318,0</kactus2:version>
	</ipxact:vendorExtensions>
</ipxact:catalog>
''',
# example from https://gist.github.com/berndca/8a9a95eb6a20a9b07e2c9a44045ec810
'berndca': '''<?xml version="1.0" encoding="UTF-8"?>
<ipxact:catalog xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:ipxact="http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
xsi:schemaLocation="http://www.accellera.org/XMLSchema/IPXACT/1685-2014/
http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd">
    <ipxact:vendor>VLSI-EDA</ipxact:vendor>
    <ipxact:library>PoC</ipxact:library>
    <ipxact:name>PoC</ipxact:name>
    <ipxact:version>0.1</ipxact:version>
    <ipxact:description> IP Core Library - Published and maintained by the Chair for VLSI Design,
        Diagnostics and Architecture, Faculty of Computer Science, Technische Universität Dresden,
        Germany http://vlsi-eda.inf.tu-dresden.de/ </ipxact:description>
    <ipxact:catalogs>
        <ipxact:ipxactFile>
            <ipxact:vlnv vendor="VLSI-EDA" library="PoC" name="uart" version="0.1"/>
            <ipxact:name>https://github.com/VLSI-EDA/PoC</ipxact:name>
            <ipxact:description>Simple UART</ipxact:description>
        </ipxact:ipxactFile>
        <ipxact:ipxactFile>
            <ipxact:vlnv vendor="VLSI-EDA" library="PoC" name="stat_Minimum" version="0.1"/>
            <ipxact:name>https://github.com/VLSI-EDA/PoC</ipxact:name>
            <ipxact:description>calculate minimums of an input stream</ipxact:description>
        </ipxact:ipxactFile>
    </ipxact:catalogs>
</ipxact:catalog>'''
}

class CatalogTests(unittest.TestCase):

    def test_catalog_catalogs_kactus2_MemoryDesign(self):
        catalog = ipyxact.ipyxact.Catalog();
        catalog.load(io.StringIO(data['kactus2-MemoryDesign']));
        self.assertTrue( hasattr(catalog, 'catalogs') );

        catalogs = catalog.catalogs;
        self.assertEqual( len(list(catalogs.ipxactFile)), 1);

        xactFile = catalogs.ipxactFile[0];
        self.assertEqual( xactFile.name, '../../../cpu.structure/cpu_example.documents/1.0/cpu_example.documents.1.0.xml' );

    def test_catalog_catalogs_berndca(self):
        catalog = ipyxact.ipyxact.Catalog();
        catalog.load(io.StringIO(data['berndca']));
        self.assertTrue( hasattr(catalog, 'catalogs') );

        catalogs = catalog.catalogs;
        self.assertEqual( len(list(catalogs.ipxactFile)), 2);

        xactFile = catalogs.ipxactFile[0];
        self.assertEqual( xactFile.name, 'https://github.com/VLSI-EDA/PoC' );

        xactFile = catalogs.ipxactFile[1];
        self.assertEqual( xactFile.name, 'https://github.com/VLSI-EDA/PoC' );

    def test_catalog_components_kactus2_spi_example(self):
        catalog = ipyxact.ipyxact.Catalog();
        catalog.load(io.StringIO(data['kactus2-spi_example']));
        self.assertTrue( hasattr(catalog, 'components') );

        components = catalog.components;
        self.assertEqual( len(list(components.ipxactFile)), 3);

        self.assertEqual( [f.name for f in components.ipxactFile], ['../../../communication.template/spi_master/1.0/spi_master.1.0.xml', '../../../communication.template/spi_slave/1.0/spi_slave.1.0.xml', '../../../other.subsystem/spi_example/1.0/spi_example.1.0.xml'] );
        self.assertEqual( [f.vlnv.vendor for f in components.ipxactFile], ['tut.fi', 'tut.fi', 'tut.fi'] );
        self.assertEqual( [f.vlnv.library for f in components.ipxactFile], ['communication.template', 'communication.template', 'other.subsystem'] );
        self.assertEqual( [f.vlnv.name for f in components.ipxactFile], ['spi_master', 'spi_slave', 'spi_example'] );
        self.assertEqual( [f.vlnv.version for f in components.ipxactFile], ['1.0', '1.0', '1.0'] );

    def test_create_catalog_catalogs(self):
        xmlstring = '''<?xml version='1.0' encoding='UTF-8'?>
<spirit:catalog xmlns:spirit="http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5">
<spirit:catalogs>
    <spirit:ipxactFile>
      <spirit:vlnv spirit:name="my_name" spirit:library="my_lib" spirit:vendor="my_vendor" spirit:version="1.1" />
      <spirit:name>../some/path</spirit:name>
    </spirit:ipxactFile>
  </spirit:catalogs>
</spirit:catalog>'''
        
        catalog = ipyxact.ipyxact.Catalog();
        
        catalogs = ipyxact.ipyxact.Catalogs();
        catalog.catalogs = catalogs;
        
        vlnv = ipyxact.ipyxact.Vlnv();
        vlnv.vendor = 'my_vendor'
        vlnv.version = '1.1'
        vlnv.name = 'my_name'
        vlnv.library = 'my_lib'
        
        ipxactFile = ipyxact.ipyxact.IpxactFile();
        ipxactFile.name = '../some/path'
        ipxactFile.vlnv = vlnv
        
        catalogs.ipxactFile.append( ipxactFile );
        
        myout = io.StringIO();    
        catalog.write(myout,indent='  ')
        
        expected = ET.fromstring(xmlstring)
        actual = ET.fromstring(myout.getvalue())
        self.assertTrue( xml_compare(expected, actual, None) )

def main():
    unittest.main(verbosity=2, )

if __name__ == '__main__':
    main()
