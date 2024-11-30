package Days;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Four {
	
	public static int[] gameTrack = new int[202];
	
	public static void main (String[] args) {
		
		int score = 0;
		int games = 0;
		
		// 0 = firstCard
		int cardCount = 1;

		try {
			File file = new File("C:\\Users\\tsutter\\Documents\\AdventOfCode\\input_4.txt");
			Scanner sc = new Scanner(file);
			
			for (int i = 0; i < gameTrack.length; i++) {
				gameTrack[i] = 1;
//				System.out.println(gameTrack[i]);
			}
//			System.out.println(gameTrack.length);
			
			while (sc.hasNextLine()) {
				String data = sc.nextLine();
				score += checkNumbs(data);
				checkNumbs(data, cardCount);
				cardCount++;
			}			

		} catch (FileNotFoundException e) {
			System.out.println("File not found");
		}
		for (int i = 0; i < gameTrack.length; i++) {
			games += gameTrack[i];
//			System.out.println(gameTrack[i]);
		}
		
		
		System.out.println("Part 1: " + score);
		System.out.println("Part 2: " + games);
	}

	
	
	private static void checkNumbs(String data, int card) {
		int game_2 = 0;
		
		String[] splits = data.split(":");
		String[] numbs = splits[1].split("\\|");
		String[] winNumb = numbs[0].trim().split(" ");
		String[] checkNumb = numbs[1].trim().split(" ");
		
		int[] winInt = new int[winNumb.length];
		Map<Integer, Integer> checkMap = new HashMap<Integer, Integer>();
		
		for (int i = 0; i < winNumb.length; i++) {
			if (winNumb[i] != "") {
				winInt[i] = Integer.parseInt(winNumb[i]);
			}
		}

		
		for (int i = 0; i < checkNumb.length; i++) {
			if (checkNumb[i] != "") {
				checkMap.put(Integer.parseInt(checkNumb[i]), null);			
			}
		}
		
		
		for (int numb : winInt) {
			if (checkMap.containsKey(numb)) {			
				game_2 ++;
			}
		}
		System.out.println("Matching Numbers on " + card + " are " + game_2);
		
		
		for (int i = 0; i < gameTrack[card -1]; i++) {
			for (int j = card; j < card + game_2; j++) {
				if (j < 202) {
					gameTrack[j] += 1;
				}		
			}
		}
		
		
		
	}

	// Part 1 Method
	private static int checkNumbs(String data) {
		int game = 0;

		String[] splits = data.split(":");
		String[] numbs = splits[1].split("\\|");
		String[] winNumb = numbs[0].trim().split(" ");
		String[] checkNumb = numbs[1].trim().split(" ");
		
		int[] winInt = new int[winNumb.length];
		Map<Integer, Integer> checkMap = new HashMap<Integer, Integer>();
		
		for (int i = 0; i < winNumb.length; i++) {
			if (winNumb[i] != "") {
				winInt[i] = Integer.parseInt(winNumb[i]);
			}
		}

		
		for (int i = 0; i < checkNumb.length; i++) {
			if (checkNumb[i] != "") {
				checkMap.put(Integer.parseInt(checkNumb[i]), null);			
			}
		}
		
		
		for (int numb : winInt) {
			if (checkMap.containsKey(numb)) {
//				System.out.print(numb + " ");
				if (game == 0) {
					game = 1;
					
				} else {
					game *= 2;

				}
			}	

		}
		return game;
	}

}








