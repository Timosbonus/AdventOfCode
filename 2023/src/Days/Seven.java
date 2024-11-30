package Days;

import java.io.File;
import java.io.FileNotFoundException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Seven {
	
	 // jede line in ein array, dann das array sortieren nach den kriterien, dann array in gesamtarray , durchlaufen und den count ausgeben
	
	 static ArrayList<String[]> handList = new ArrayList<String[]>();

	 static ArrayList<String[]> highCard = new ArrayList<String[]>();
	 static ArrayList<String[]> onePair = new ArrayList<String[]>();
	 static ArrayList<String[]> twoPairs = new ArrayList<String[]>();
	 static ArrayList<String[]> threePair = new ArrayList<String[]>();
	 static ArrayList<String[]> fullHouse = new ArrayList<String[]>();
	 static ArrayList<String[]> fourPair = new ArrayList<String[]>();
	 static ArrayList<String[]> fivePair = new ArrayList<String[]>();
	 
	 
	public static void main (String[] args) {

		try {
			File file = new File("C:\\Users\\tsutter\\Documents\\AdventOfCode\\input_7.txt");
			Scanner sc = new Scanner(file);
			

			
			while (sc.hasNextLine()) {
				String data = sc.nextLine();
				checkHand(data);

			}			

		} catch (FileNotFoundException e) {
			System.out.println("File not found");
		}
		
		highCard = sortLists(highCard);
		onePair = sortLists(onePair);
		twoPairs = sortLists(twoPairs);
		threePair = sortLists(threePair);
		fullHouse = sortLists(fullHouse);
		fourPair = sortLists(fourPair);
		fivePair = sortLists(fivePair);
		
		
		
		handList.addAll(highCard);
		handList.addAll(onePair);
		handList.addAll(twoPairs);
		handList.addAll(threePair);
		handList.addAll(fullHouse);
/*		for (String[] card : handList) {
			System.out.println(card[0] + " " + card[1]);
		}
		System.out.println(); */
		handList.addAll(fourPair);
		handList.addAll(fivePair);
		
		
		long sumPartOne = 0;
		int count = 1;
		for (String[] card : handList) {
			System.out.println(card[0] + " " + card[1]);
			sumPartOne = (Integer.parseInt(card[1]) * count) + sumPartOne;
			count++;
		}
		
				
		System.out.println("Part 1: " + sumPartOne);
		System.out.println("Part 2: ");
	}
	

	
	private static ArrayList<String[]> sortLists(ArrayList<String[]> cardList) {
		List<Character> customOrder = Arrays.asList('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2');
		Map<Character, Integer> orderMap = new HashMap<>();
		
		for (int i = 0; i < customOrder.size(); i++) {
	            char character = customOrder.get(i);
	            orderMap.put(character, i);
		}
				
		
//		System.out.println(orderMap.toString());
		
		
		boolean swapped = true;
		
		while (swapped) {
			swapped = false;
			for (int i = 0; i < cardList.size() - 1; i++) {
				int j = i + 1;
				String[] first = cardList.get(i);
				String[] second = cardList.get(j);

				for (int k = 0; k < 5; k++) {
					char aToCompare = first[0].charAt(k);
					char bToCompare = second[0].charAt(k);
					if (aToCompare == bToCompare) {
						continue;
					}
					if (orderMap.get(aToCompare) < orderMap.get(bToCompare)) {
//						System.out.println(first[0] + " " + second[0] + " " + aToCompare + " " + bToCompare);
						String[] temp = cardList.get(i);
						cardList.remove(i);
						cardList.add(j, temp);
						
						swapped = true;
						break;
					} else {
						break;
					}
						
				}		
			}

		}
			
		return cardList;
	}
	
		
	
	private static void checkHand(String data) {
		
		String[] split = data.split(" ");
		String hand = split[0];
				
		HashMap<Character, Integer> handCount = new HashMap<Character, Integer>();
		
		
		
		for (int i = 0; i < 5; i++) {
			char card = hand.charAt(i);
			if (handCount.containsKey(card)) {
				handCount.put(card, handCount.get(card) + 1);
			} else {
				handCount.put(card, 1);
			}	
		}
		
		if (handCount.size() == 5) {
			// high Card
			highCard.add(split);
		} else if (handCount.size() == 4) {
			// one pair
			onePair.add(split);
		} else if (handCount.size() == 3) {
			// either two pairs or one three pair
			int maxCount = 0;
			for (Map.Entry<Character, Integer> entry : handCount.entrySet()) {
				if (maxCount < entry.getValue()) {
					maxCount = entry.getValue();
				} 
			}
			if (maxCount == 2) {
				twoPairs.add(split);
			} else {
				threePair.add(split);
			}
		} else if (handCount.size() == 2) {
			for (Map.Entry<Character, Integer> entry : handCount.entrySet()) {
				if (entry.getValue() == 4 || entry.getValue() == 1) {
					fourPair.add(split);
					break;
				} else {
					fullHouse.add(split);
					break;
				}
			}
			System.out.println();
			
		} else {
			fivePair.add(split);
		}
	
	}
	
	


}
