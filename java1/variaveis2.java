class Festa {
	public static void main(String[] args) {
		int idadeVisitante = 19;
		boolean amigoDoDono = false;
		
		if (idade >= 60) {
			System.out.println("Aproveite a melhor idade");
		}
		else if (idadeVisitante >= 18 && amigoDoDono){
			System.out.println("Entre na festa!");
		} else {
			System.out.println("Volte para casa!");
		}
	}
}