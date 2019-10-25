# Mineracao-de-Dados

Repositório pessoal da disciplina de Mineração de Dados.
<br/>
Repositório oficial da disciplina [Mineração de Dados](https://github.com/liviaalmada/mineracao-de-dados-20192) 2019.2
<br/>
Professora: [Lívia Almada](https://github.com/liviaalmada)
<br/>

configuração de themas para o Jupter.
<br/>
```
jt -t <theme_name>
```
Lista de theme
onedork
<br/>
grade3
<br/>
oceans16
<br/>
chesterish
<br/>
monokai
<br/>
solarizedl
<br/>
solarizedd
<br/>
voltar para o padrão defaut

1. verifique se o servidor do notebook não está funcionando.
2. execute ``` jt -r ```
3. exclua os dois diretórios listados por ``` jt -r ```
4. reinicie o seu servidor
5. (se ainda não redefinir) Force o navegador a redefinir seu cache. No chrome, você pode fazer isso com os devtools abertos F12. Eu não acho que o mini servidor Jupyter possa rastrear alterações em todos os arquivos dependentes.
6. se você ainda estiver com problemas, execute ``` curl 'http: // localhost: 8888 / custom / custom.css' ``` na linha de comando e inspecione manualmente o arquivo css que está sendo retornado se tiver CSS nele após todas essas etapas, você pode continuar seguindo o debuga mas neste momento você deve ser tudo de bom.
7. reinicie seu notebook jupyter no modo de debug ``` Jupiter notebook --debug ```
8. no início da depuração, ele tentou carregar a configuração de vários diretórios, dependendo da instalação e da estrutura do pacote. O arquivo custom / custom.css deve estar em um desses diretórios. Encontre-o e exclua-o.

https://github.com/dunovank/jupyter-themes/issues/86