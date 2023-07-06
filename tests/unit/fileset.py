import unittest
import io
from ipyxact.ipyxact import Component

data = '''<?xml version="1.0" encoding="UTF-8"?>
<spirit:component xmlns:kactus2="http://funbase.cs.tut.fi/" xmlns:spirit="http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5 http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5/index.xsd">
	<spirit:vendor>org.example</spirit:vendor>
	<spirit:library>example_lib</spirit:library>
	<spirit:name>example_name</spirit:name>
	<spirit:version>example_version</spirit:version>
	<spirit:fileSets>
		<spirit:fileSet>
			<spirit:name>rtl_files</spirit:name>
			<spirit:file>
				<spirit:name>rtl/verilog/example_top.v</spirit:name>
				<spirit:fileType>verilogSource</spirit:fileType>
				<spirit:isIncludeFile spirit:externalDeclarations="false">false</spirit:isIncludeFile>
			</spirit:file>
			<spirit:file>
				<spirit:name>rtl/verilog/example_core.v</spirit:name>
				<spirit:fileType>verilogSource</spirit:fileType>
				<spirit:isIncludeFile spirit:externalDeclarations="false">false</spirit:isIncludeFile>
			</spirit:file>
		</spirit:fileSet>
		<spirit:fileSet>
			<spirit:name>tb_files</spirit:name>
			<spirit:file>
				<spirit:name>bench/example_tb.v</spirit:name>
				<spirit:fileType>verilogSource</spirit:fileType>
				<spirit:isIncludeFile spirit:externalDeclarations="false">false</spirit:isIncludeFile>
			</spirit:file>
		</spirit:fileSet>
	</spirit:fileSets>
</spirit:component>
'''

class FilesetTests(unittest.TestCase):

    def test_dummy(self):
        self.assertEqual(1, 1)

    def test_component(self):
        component = Component();
        component.load(io.StringIO(data));
        self.assertTrue( hasattr(component, 'fileSets') );

        filesets = component.fileSets;
        self.assertEqual( len(list(filesets.fileSet)), 2);

        fileset = filesets.fileSet[0];
        self.assertEqual( fileset.name, 'rtl_files' );
        files = list(fileset.file);
        self.assertEqual( len(files), 2 );
        self.assertEqual( [f.name for f in files], ['rtl/verilog/example_top.v', 'rtl/verilog/example_core.v'] );

        fileset = filesets.fileSet[1];
        self.assertEqual( fileset.name, 'tb_files' );
        files = list(fileset.file);
        self.assertEqual( len(files), 1 );
        self.assertEqual( [f.name for f in files], ['bench/example_tb.v'] );

def main():
    unittest.main(verbosity=2, )

if __name__ == '__main__':
    main()
