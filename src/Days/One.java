package Days;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner; 
public class One {
	
    private static final Map<String, Integer> wordToNumberMap = new HashMap<>();

    static {
        wordToNumberMap.put("one", 1);
        wordToNumberMap.put("two", 2);
        wordToNumberMap.put("three", 3);
        wordToNumberMap.put("four",4);
        wordToNumberMap.put("five",5);
        wordToNumberMap.put("six",6);
        wordToNumberMap.put("seven",7);
        wordToNumberMap.put("eight",8);
        wordToNumberMap.put("nine",9);
    }
	
	public static void main (String[] args) {
		
		int sum = 0;

		try {
			File file = new File("C:\\Users\\tsutter\\Documents\\AdventOfCode\\input_1.txt");
			Scanner sc = new Scanner(file);
			while (sc.hasNextLine()) {
				String data = sc.nextLine();
				sum += returnNumbs(convertLetters(data));
			}
			sc.close();
			
			
		} catch (FileNotFoundException e) {
			System.out.println("File not found");
		}
		System.out.println(sum);
	}
	
	
	private static int returnNumbs(String line){
		int first = 0;
		int last = 0;
		boolean found = false;

		for (int i = 0; i < line.length(); i++) {
			char a = line.charAt(i);
			
			if (Character.isDigit(a) && !found) {
				first += Character.getNumericValue(a) * 10;
				last = Character.getNumericValue(a);
				found = true;
			} else if (Character.isDigit(a)) {
				last = Character.getNumericValue(a);
			}
		}
		System.out.println(first + last);
		return first + last;
	}
	
	
	private static String convertLetters(String line) {
		String first = "";
		for (int i = 0; i < line.length(); i++) {
			first = first + line.charAt(i);
					
			for (String key : wordToNumberMap.keySet()) {
				
				if (first.contains(key)) {
					first = first.replaceAll(key, Integer.toString(wordToNumberMap.get(key)));
				}				
			}		
		}
		String second = "";
		for (int i = line.length() - 1; i >= line.length() / 2; i--) {
			second = line.charAt(i) + second;
					
			for (String key : wordToNumberMap.keySet()) {
				
				if (second.contains(key)) {
					second = second.replaceAll(key, Integer.toString(wordToNumberMap.get(key)));
				}				
			}		
		}
		System.out.println(line);
		System.out.println(first + second);
		return first + second;
	}
	
	private static String wordsToNumbers(String line) {
		String first = "";
		boolean stop = false;
		for (int i = 0; i < line.length(); i++) {
			first = first + line.charAt(i);
			
			for (String key : wordToNumberMap.keySet()) {
				
				if (first.contains(key)) {
					first = first.replaceAll(key, Integer.toString(wordToNumberMap.get(key)));
					stop = true;
					break;
				}				
			}
			if (stop) {
				stop = false;
				break;
			}
		}
		
		
		String second = "";
		for (int i = line.length() - 1; i >= 0; i--) {
			second = line.charAt(i) + second;
					
			for (String key : wordToNumberMap.keySet()) {
				
				if (second.contains(key)) {
					second = second.replaceAll(key, Integer.toString(wordToNumberMap.get(key)));
					stop = true;
					break;
				}				
			
			}
			if (stop) {
				stop = false;
				break;
			}
		}
		
		System.out.println(first + second);
		
		return first + second;
	}
	
}
	
	
	
