package Days;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Nine {
	
	
	
	public static void main (String[] args) {
		
		ArrayList<ArrayList<Integer>> numbRowsFirst = new ArrayList<>();
		ArrayList<ArrayList<Integer>> numbRowsSecond = new ArrayList<>();

		try {
			File file = new File("C:\\Users\\tsutter\\Documents\\AdventOfCode\\input_9.txt");
			Scanner sc = new Scanner(file);
			

			
			while (sc.hasNextLine()) {
				String data = sc.nextLine();
				String[] sNumbs = data.split(" ");
				ArrayList<Integer> row = new ArrayList<>();
				
				for (int i = 0; i < sNumbs.length; i++) {
					try {
						row.add(Integer.parseInt(sNumbs[i]));
					} catch (Exception e) {
						continue;
					}
				}
			
				numbRowsFirst.add(row);
				numbRowsSecond.add(row);

			}			
			
		} catch (FileNotFoundException e) {
			System.out.println("File not found");
		}
		
		int resultPartOne = 0;
		int resultPartTwo = 0;
/*		for (ArrayList<Integer> row : numbRowsFirst) {
			resultPartOne += findNext(row);
		} */ 
		for (ArrayList<Integer> row : numbRowsSecond) {
			resultPartTwo += findNextReverse(row);
		} 
			
		
		
		System.out.println("Part 1: " + resultPartOne);
		System.out.println("Part 2: " + resultPartTwo);
	}
	
	
	private static int findNextReverse(ArrayList<Integer> current) {
		
		ArrayList<ArrayList<Integer>> findNextArray = new ArrayList<>();
		findNextArray.add(current);
		
		// checks if sum from line is not 0
		while (sumArray(findNextArray.get(findNextArray.size() - 1)) != 0) {
			ArrayList<Integer> diffBetweenNumbs = new ArrayList<Integer>();
			ArrayList<Integer> lastRow = findNextArray.get(findNextArray.size() - 1);
			for (int i = 0; i < lastRow.size() - 1; i++) {
				diffBetweenNumbs.add(lastRow.get(i + 1) - lastRow.get(i));
			}
			findNextArray.add(diffBetweenNumbs);
		}
		
		// test print
		
		
		for (int j = findNextArray.size() - 1; j > 0; j--) {
			ArrayList<Integer> currentRow = findNextArray.get(j);
			ArrayList<Integer> nextRow = findNextArray.get(j - 1);
			
			findNextArray.get(j - 1).add(0, nextRow.get(0) - currentRow.get(0));
			
		}
		
		
		for (ArrayList<Integer> test : findNextArray) {
			for (int t : test) {
				System.out.print(t + " ");
			}
			System.out.println();
		} 
		
		//works
		return findNextArray.get(0).get(0);
	}

	
	
	
	private static int findNext(ArrayList<Integer> current) {
		
		ArrayList<ArrayList<Integer>> findNextArray = new ArrayList<>();
		findNextArray.add(current);
		
		// checks if sum from line is not 0
		while (sumArray(findNextArray.get(findNextArray.size() - 1)) != 0) {
			ArrayList<Integer> diffBetweenNumbs = new ArrayList<Integer>();
			ArrayList<Integer> lastRow = findNextArray.get(findNextArray.size() - 1);
			for (int i = 0; i < lastRow.size() - 1; i++) {
				diffBetweenNumbs.add(lastRow.get(i + 1) - lastRow.get(i));
			}
			findNextArray.add(diffBetweenNumbs);
		}
		
		// test print
		/*
		for (ArrayList<Integer> test : findNextArray) {
			for (int t : test) {
				System.out.print(t + " ");
			}
			System.out.println();
		} */
		
		for (int j = findNextArray.size() - 1; j > 0; j--) {
			ArrayList<Integer> currentRow = findNextArray.get(j);
			ArrayList<Integer> nextRow = findNextArray.get(j - 1);
			findNextArray.get(j - 1).add(currentRow.get(currentRow.size() - 1) + nextRow.get(nextRow.size() - 1));
			System.out.println(currentRow.toString());
		}
		
		
		//works
		return findNextArray.get(0).get(findNextArray.get(0).size() - 1);
	}
	
	
	private static int sumArray(ArrayList<Integer> row) {
		int sum = 0;
		for (int i : row) {
			sum += i;
		}
		return sum;
	}


}
