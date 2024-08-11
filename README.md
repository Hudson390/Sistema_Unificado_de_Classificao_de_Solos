<h1>Ferramenta de Classificação de Solos</h1>
<p>Este script em Python classifica solos com base em diversos parâmetros, como análise granulométrica, limite de liquidez e índice de plasticidade. A classificação segue práticas padrão de engenharia geotécnica e fornece descrições detalhadas do tipo de solo.</p>
<h2>Funcionalidades</h2>
<ul>
  <li><strong>Classificação de Solos</strong>: Com base no percentual de material que passa nas peneiras 200 e 4, limite de liquidez (LL) e índice de plasticidade (IP), o script categoriza o solo em vários tipos, como grosso, fino, pedregulho ou areia, com distinções adicionais para solos bem graduados, mal graduados, argilosos ou siltosos.</li>
  <li><strong>Entrada Interativa</strong>: O script solicita valores de entrada ao usuário e fornece resultados de classificação de solo em tempo real.</li>
  <li><strong>Limpeza do Terminal</strong>: Limpa automaticamente o terminal após cada iteração para proporcionar uma interface de usuário limpa.</li>
</ul>

<h2>Requisitos</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Um sistema operacional com acesso ao terminal/comando (Windows, Linux ou macOS)</li>
    </ul>

  <h2>Uso</h2>
    <ol>
        <li>Clone este repositório para sua máquina local:
            <pre><code>git clone https://github.com/seuusuario/ferramenta-classificacao-solos.git
cd ferramenta-classificacao-solos</code></pre>
        </li>
        <li>Execute o script:
            <pre><code>python classificar_solo.py</code></pre>
        </li>
        <li>Siga as instruções na tela para inserir os dados necessários:
            <ul>
                <li>Percentual que passa na peneira 200</li>
                <li>Percentual que passa na peneira 4</li>
                <li>Limite de Liquidez (LL)</li>
                <li>Índice de Plasticidade (IP)</li>
            </ul>
        </li>
        <li>Veja os resultados da classificação exibidos no terminal.</li>
        <li>Escolha se deseja continuar classificando mais amostras ou sair do programa.</li>
    </ol>

  <h2>Exemplo</h2>
    <pre><code>
Percentual que passa na peneira 200: 45
Percentual que passa na peneira 4: 60
Limite de liquidez: 35
Índice de plasticidade: 15

Classificação do Solo:
Solo Grosso
Areia Argilosa
    </code></pre>

  <h2>Licença</h2>
    <p>Este projeto está licenciado sob a Licença MIT - veja o arquivo <a href="LICENSE">LICENSE</a> para mais detalhes.</p>

  <h2>Contribuindo</h2>
    <p>Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request ou abrir uma Issue para quaisquer melhorias ou correções de bugs.</p>

  <h2>Contato</h2>
    <p>Para qualquer dúvida ou sugestão, sinta-se à vontade para entrar em contato por e-mail: <a href="mailto:hudsoncdiniz@gmail.com">hudsoncdiniz@gmail.com</a>.</p>
