
/*
class Loops {
	public static void main(String[] args) {
		for (int i = 3; i < 100; i += 3) {
			System.out.println(i + "\n");
		}
	}
}



class Fatorial {
	public static void main(String[] args) {
		for (long i = 1; i <= 30; i++) {
			long fatorial = 1;
			for (long j = 1; j <= i; j++) {
				fatorial = fatorial * j;
			}
			System.out.println("O fatorial de " + i + " é : " + fatorial);
		}
	}
}

*/

class Exercicio {
	public static void main(String[] args) {
		int x = 13;

		System.out.print(x + " > ");
		
		while(x != 1) {
			if (x % 2 == 0) {
				x = x / 2;
			} else {
				x = 3 * x + 1;
			}
			System.out.print(x + " > ");
		}
	}
}
