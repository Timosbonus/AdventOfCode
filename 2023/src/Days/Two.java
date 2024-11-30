package Days;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Two {
	
	public static void main (String[] args) {
		
		int sum = 0;

		try {
			File file = new File("C:\\Users\\tsutter\\Documents\\AdventOfCode\\input_2.txt");
			Scanner sc = new Scanner(file);
			while (sc.hasNextLine()) {
				String data = sc.nextLine();
				sum += splitLine(data);
			}
			
			System.out.println(sum);

		} catch (FileNotFoundException e) {
			System.out.println("File not found");
		}
	}
	
	private static int splitLine(String line) {
		// parts[1] = number , "[, . ' : ;]+"
		int gameNum = 0;
		boolean valid = true;
		
		int greenMin = 0;
		int redMin = 0;
		int blueMin = 0;
		
		String[] parts = line.split(":");	
		String[] games = parts[1].split(";");
		
		for (String game : games) {
			String[] cubes = game.split(",");
			for (String cube : cubes) {
				String[] colourAndNumb = cube.split("\\s+");
				
				int number = Integer.parseInt(colourAndNumb[1]);
				String colour = colourAndNumb[2];
				
				
				
				
				if (colour.equals("green") && number > greenMin) {
					greenMin = number;
				}
				if (colour.equals("red") && number > redMin) {
					redMin = number;
				}
				if (colour.equals("blue") && number > blueMin) {
					blueMin = number;
				}
				}
				
				
			}
		
		
		return greenMin * redMin * blueMin;
	}
}
