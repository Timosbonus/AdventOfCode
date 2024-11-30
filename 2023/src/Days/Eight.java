package Days;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Eight {

    static HashMap<String, String[]> searchMap = new HashMap<>();
    static String pattern;

    public static void main(String[] args) {

        String filePath = "C:\\Users\\tsutter\\Documents\\AdventOfCode\\input_test.txt";

        int count = 0;

        try (Scanner scanner = new Scanner(new File(filePath))) {

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                if (count < 1) {
                    pattern = line;
                    count++;
                } else {
                    fillMap(line);
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        
        ArrayList<String> startVals = new ArrayList<String>();
        for (Map.Entry<String, String[]> entry : searchMap.entrySet()) {
        	if (entry.getKey().charAt(2) == 'A') {
        		startVals.add(entry.getKey());
        	}
        }
        
        
        System.out.println("Part one: " + searchPartOne());
        
        
        int[] durations = new int[startVals.size()];
        for (int i = 0 ; i < startVals.size(); i++) {
        	durations[i] = searchPartTwo(startVals.get(i));
        }
        System.out.println(Arrays.toString(durations));
        System.out.println(kgV(durations));
        
    }
    
    private static long kgV(int[] vals) {
    	int product = vals[0];
    	for (int i = 1; i < vals.length; i++) {
    		product *= vals[i];
    	}
    	return Math.abs(product) / ggt(vals);
    }
    
    private static int ggt(int[] vals) {
    	int low = vals[0];
    	for (int i : vals) {
    		if (i < low) {
    			low = i;
    		}
    	}
    	int ggt = 1;
    	for (int j = low; j > 1; j--) {
    		ggt = j;
    		boolean flag = true;
    		for (int val : vals) {
    			if (val % ggt != 0) {
    				flag = false;
    			}
    			
    		}
    		if (flag) break;
    	}
    		
    	return ggt;
    }
   
    
    
    private static int searchPartTwo(String start) {
        int steps = 0;

        do {
            for (int i = 0 ; i < pattern.length(); i++) {
                char currentDir = pattern.charAt(i);
                String[] list = searchMap.get(start);

                
                if (currentDir == 'L') {
                    start = list[0];
                } else {
                    start = list[1];
                }
                
                steps++;
                if (start.charAt(2) == 'Z') {
                    break;
                }
            } 
                             
        } while (start.charAt(2) != 'Z');

        return steps;
    }
   
    
    
    
    private static int searchPartOne() {
        String currentString = "AAA";
        int steps = 0;

        do {
            for (int i = 0 ; i < pattern.length(); i++) {
                char currentDir = pattern.charAt(i);
                String[] list = searchMap.get(currentString);

                
                if (currentDir == 'L') {
                    currentString = list[0];
                } else {
                    currentString = list[1];
                }
                
                steps++;
                if (currentString.equals("ZZZ")) {
                    break;
                }
            } 
                             
        } while (!currentString.equals("ZZZ"));

        return steps;
    }
    
    private static void fillMap(String line) {
        String[] parts = line.split("\\W");
        ArrayList<String> patts = new ArrayList<>();
        for (String i : parts) {
            if (!Objects.equals(i, "")) {
                patts.add(i);
            }
        }
        searchMap.put(patts.get(0), new String[] {patts.get(1), patts.get(2)});
    }
}
