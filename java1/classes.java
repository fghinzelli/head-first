class Conta {
	
	Pessoa titular;
	int agencia;
	int numero;
	double saldo;

	void deposita(double valorASerDepositado) {
		this.saldo += valorASerDepositado;

	}

	void saca(double valorASerSacado) {		
		if (this.saldo >= valorASerSacado) {
			this.saldo -= valorASerSacado;	
		}
	}

	void transfere(double valor, Conta destino) {
		this.saldo -= valor;
		destino.saldo += valor;
	}
}

class Pessoa {
	String nome;
	String cpf;
	String dataNascimento;
}

class ProgramaConta {
	public static void main(String[] args) {
		Conta fernando = new Conta();

		fernando.numero = 123;
		fernando.saldo = 800.0;
		fernando.titular = new Pessoa();
		fernando.titular.nome = "Fernando Ghinzelli";
		fernando.titular.cpf = "123443354";
		fernando.titular.dataNascimento = "14/08/1985";
		fernando.agencia = 842;

		System.out.println(fernando.titular.nome);

		fernando.deposita(100);
		fernando.saca(50);

		Conta mariel = new Conta();
		mariel.numero = 342;
		mariel.saldo = 1200.0;

		mariel.deposita(1100);

		fernando.transfere(100, mariel);

		System.out.println(fernando.saldo);
		System.out.println(mariel.saldo);
	}



}