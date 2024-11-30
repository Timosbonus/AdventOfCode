package Days;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Three {
	
	private static final int None = 0;

	public static ArrayList<ArrayList<String>> list = new ArrayList<>();
	public static ArrayList<ArrayList<String>> gearArray = new ArrayList<>();
	public static long sumGear = 0;
	
	public static void main (String[] args) {
		

		try {
			File file = new File("C:\\Users\\tsutter\\Documents\\AdventOfCode\\input_3.txt");
			Scanner sc = new Scanner(file);
			while (sc.hasNextLine()) {
				String data = sc.nextLine();
				ArrayList<String> line = new ArrayList<>();
				for (int i = 0; i < data.length(); i++) {
					line.add(String.valueOf(data.charAt(i)));
				}
				list.add(line);
			}
			checkList();		

		} catch (FileNotFoundException e) {
			System.out.println("File not found");
		}
	}
	
	private static void checkList() {
		
		int sum = 0;
		
		
		
		for (int i = 0; i < list.size(); i++) {
			int innerIndex = -1;
			int outerIndex = -1;
			
			for (int j = 0; j < list.get(i).size(); j++) {
				String currentSymbol = list.get(i).get(j);
				
				if (isValidInteger(currentSymbol) == true) {
					if (innerIndex == -1) {
						innerIndex = j;
					}
					outerIndex = j;
				}
				if ((!isValidInteger(currentSymbol) && innerIndex != -1 && outerIndex != -1) || (isValidInteger(currentSymbol) && j == list.get(i).size()-1)) {
					
					
					
					if (checkRows(innerIndex, outerIndex, i,0)) { 
						String s = "";
						for (int k = innerIndex; k <= outerIndex; k++) {
							s = s + list.get(i).get(k);
							
						}
						sum += Integer.parseInt(s);

						System.out.println(Integer.parseInt(s));
					}
					
					
					
					innerIndex = -1;
					outerIndex = -1;
								
				}	
			}
		}
		System.out.println("Part 1 : " + sum);
		System.out.println("Part 2 : " + sumGear);
	}
	
	// Logik: Zahl passt, check nach Stern, speicher die Zahl, Y-Stern, X-Stern -> checke jede weitere Zahl, wenn Stern = Y-Stern, X-Stern subtrahier von der Summe zahl 1, lösch aus dem Array, addier produkt
	
	private static int checkGearArray(int i, int j, String s) {
		int value = 0;
		
//		System.out.print(String.valueOf(i));
				
		for (int k = 0; k < gearArray.size(); k++) {
			if (gearArray.get(k).get(0).equals(String.valueOf(i)) && gearArray.get(k).get(1).equals(String.valueOf(j))  && s != gearArray.get(k).get(2)) {
				
				value = Integer.parseInt(s) * Integer.parseInt(gearArray.get(k).get(2));

				
				gearArray.remove(k);
			} else {
				sumGear += Integer.parseInt(s);
			}
		}
		
		return value;
	}
	
	private static boolean checkRows(int inner, int outer, int currentRow,int overload) {
		boolean out = false;
		int yMax = currentRow == list.size() -1  ? list.size() -1: currentRow+1;
		int yMin = currentRow == 0  ? 0 : currentRow -1;
		int xMax = outer == list.get(currentRow).size() -1  ? outer : outer +1;
		int xMin = inner == 0  ? 0 : inner -1;
		
		for (int i = yMin; i <= yMax; i++) {
			for (int j = xMin; j <= xMax; j++) {
				if(checkField(list.get(i).get(j))) {
					out =  true;
					
					if(list.get(i).get(j).equals("*")) {
						
						
						String s = "";
						for (int k = inner; k <= outer; k++) {
							s = s + list.get(currentRow).get(k);
						}
						ArrayList<String> gearStar = new ArrayList<String>();
						gearStar.add(String.valueOf(i));
						gearStar.add(String.valueOf(j));
						gearStar.add(s);
						
						gearArray.add(gearStar);
						
//						System.out.println(gearArray.toString());
						
						sumGear += checkGearArray(i,j,s);
					
						
					
					
					}
					
				}
				
			}

		}

		return out;
	}
	
		
	private static boolean checkField(String place) {
		return !place.equals(".") && !Character.isDigit(place.charAt(0));
	}
	
	private static boolean isValidInteger(String symbol) {
		try {
			Integer.parseInt(symbol);
			return true;
		} catch(Exception f) {
			return false;
		}
	}
	
	

}
