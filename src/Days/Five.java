package Days;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Five {
	
	
	
	public static void main (String[] args) {

		try {
			File file = new File("C:\\Users\\tsutter\\Documents\\AdventOfCode\\input_test.txt");
			Scanner sc = new Scanner(file);
			

			
			while (sc.hasNextLine()) {
				String data = sc.nextLine();

			}			

		} catch (FileNotFoundException e) {
			System.out.println("File not found");
		}

		
		
		System.out.println("Part 1: ");
		System.out.println("Part 2: ");
	}


}
