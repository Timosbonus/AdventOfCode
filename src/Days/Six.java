package Days;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Six {
	
	static ArrayList<Integer> timeList = new ArrayList<Integer>();
	static ArrayList<Integer> distanceList = new ArrayList<Integer>();
	static long twoTime = 0;
	static long twoDistance = 0;
	
	public static void main (String[] args) {
		
		int wins_1 = 0;
		long wins_2 = 0;

		try {
			File file = new File("C:\\Users\\tsutter\\Documents\\AdventOfCode\\input_6.txt");
			Scanner sc = new Scanner(file);
			
			fillLists(sc.nextLine(), sc.nextLine());
			wins_1 = calculateWinnings();
			wins_2 = calculateWinnings(0);

			
			
		} catch (FileNotFoundException e) {
			System.out.println("File not found");
		}

		
		System.out.println("Part 1: " + wins_1);
		System.out.println("Part 2: " + wins_2);
	}
	
	private static void fillLists(String inputTime,String inputDistances) {
		String time = "";
		String dist = "";
		
		String[] splitTimes = inputTime.split(":");
		String[] stringTimes = splitTimes[1].split(" ");
		
		for (int i = 0; i < stringTimes.length; i++) {
			stringTimes[i].trim();
			if (stringTimes[i] != "") {
				timeList.add(Integer.parseInt(stringTimes[i]));
				time = time + stringTimes[i];
			}			
		}
		
		twoTime = Long.parseLong(time);
		
		String[] splitDistance = inputDistances.split(":");
		String[] stringDistances = splitDistance[1].split(" ");
		
		for (int i = 0; i < stringDistances.length; i++) {
			stringDistances[i].trim();
			if (stringDistances[i] != "") {
				distanceList.add(Integer.parseInt(stringDistances[i]));
				dist = dist + stringDistances[i];
			}			
		}
		twoDistance = Long.parseLong(dist);
		
		System.out.println("Time: " + time + " Dist: " + dist);
		
		
	}
	
	private static long calculateWinnings(int overload) {
		long wins = 0;

		for (int i = 0; i <= twoTime; i++) {
			if (i * (twoTime - i) > twoDistance) {
				wins += 1;
			}		
		}
		
		return wins;
	}
	
	private static int calculateWinnings() {
		int wins = 0;
		
		for (int j = 0; j < timeList.size(); j++) {
			int possi = 0;
			for (int i = 0; i <= timeList.get(j); i++) {
				if (i * (timeList.get(j) - i) > distanceList.get(j)) {
					possi += 1;
				}		
			}
			if (wins == 0) {
				wins = possi;
			} else {
				wins *= possi;
			}
		}
		
		return wins;
	}


}
