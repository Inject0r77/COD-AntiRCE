# RCE Protection for Call of Duty: Modern Warfare 3 (2011)

# ( EU )
This project provides a network protection system against Remote Code Execution (RCE) exploits in Call of Duty: Modern Warfare 3 (2011). It focuses on monitoring network traffic, blocking malicious packets, and ensuring game integrity by preventing unauthorized actions such as forced microphone activation or disabling.

Features
- RCE Exploit Protection: Intercepts and analyzes network traffic for known malicious payloads.
- Mic Command Filtering: Detects and blocks packets attempting to control the in-game microphone (force mic on/off).
- Game Process Monitoring: Ensures the game is running and monitors its associated network traffic.
- Logging System: Detailed logs for actions performed, including blocked packets and errors.

Installation and Usage:
Prerequisites
- Python Version: Ensure Python 3.10 or higher is installed.
- Dependencies: Install the required Python libraries:
pip install psutil pydivert

- Windows Platform: This project requires a Windows environment due to WinDivert.

Running the Protection System:
- Launch the main script: python main.py
 
The application will:
- Check if the game process is running.
- Intercept and analyze network traffic.
- Log all actions and block malicious packets as configured.

How It Works:
1. Game Process Check: The system verifies the game process is running before starting the network monitor.
2. Packet Interception: Using WinDivert, it captures and inspects packets matching the configured filter.
3. Malicious Payload Detection: The system scans packet payloads for harmful commands, including:
 -Exploit commands
 -Forced mic activation/deactivation
4. Packet Blocking: Detected malicious packets are dropped to prevent exploitation.

Contribution:
Contributions are welcome! Feel free to fork the repository, create issues, or submit pull requests.


# ( RU ) 
Этот проект обеспечивает систему защиты сети от эксплойтов удаленного выполнения кода (RCE) в Call of Duty: Modern Warfare 3 (2011). Он фокусируется на мониторинге сетевого трафика, блокировании вредоносных пакетов и обеспечении целостности игры путем предотвращения несанкционированных действий, таких как принудительная активация или отключение микрофона.

Функции
-
RCE Exploit Protection: перехватывает и анализирует сетевой трафик на наличие известных вредоносных данных.
- Фильтрация команд микрофона: обнаруживает и блокирует пакеты, пытающиеся управлять внутриигровым микрофоном (принудительное включение/выключение микрофона).
- Мониторинг игрового процесса: обеспечивает работу игры и отслеживает связанный с ней сетевой трафик.
-
Система журналирования: подробные журналы выполненных действий, включая заблокированные пакеты и ошибки.

Установка и использование:
Предварительные условия
- Версия Python: убедитесь, что установлен Python 3.10 или более поздней версии.
- Зависимости: установите необходимые библиотеки Python:
pip установить psutil pydivert

-
Платформа Windows: для этого проекта требуется среда Windows из-за WinDivert.

Запуск системы защиты:
- Запустите основной скрипт: python main.py.
 
Приложение будет:
- Проверьте, запущен ли игровой процесс.
- Перехватывать и анализировать сетевой трафик.
- Регистрируйте все действия и блокируйте вредоносные пакеты в соответствии с настройками.

Как это работает:
1.
Проверка игрового процесса: система проверяет запуск игрового процесса перед запуском сетевого монитора.
2. Перехват пакетов. Используя WinDivert, он перехватывает и проверяет пакеты, соответствующие настроенному фильтру.
3. Обнаружение вредоносной полезной нагрузки. Система сканирует полезные данные пакетов на наличие вредоносных команд, в том числе:
 -Эксплуатация команд
 -
Принудительная активация/деактивация микрофона
4. Блокировка пакетов. Обнаруженные вредоносные пакеты удаляются, чтобы предотвратить эксплуатацию.

Вклад:
Вклады приветствуются! Не стесняйтесь создавать форки репозитория, создавать задачи или отправлять запросы на включение.


# Disclaimer 1
(EU) - This project is for educational purposes and intended to enhance the gaming experience by mitigating security risks. It does not endorse any form of cheating or exploitation.
(RU) - Этот проект предназначен для образовательных целей и призван улучшить игровой процесс за счет снижения рисков безопасности. Он не поддерживает какие-либо формы мошенничества или эксплуатации.

<h1>Disclaimer 2</h1>
<p>Last updated: December 04, 2024</p>
<h2>Interpretation and Definitions</h2>
<h3>Interpretation</h3>
<p>The words of which the initial letter is capitalized have meanings defined under the following conditions.
The following definitions shall have the same meaning regardless of whether they appear in singular or in plural.</p>
<h3>Definitions</h3>
<p>For the purposes of this Disclaimer:</p>
<ul>
<li>
<p><strong>Company</strong> (referred to as either &quot;the Company&quot;, &quot;We&quot;, &quot;Us&quot; or &quot;Our&quot; in this Disclaimer) refers to Test proxy generator.</p>
</li>
<li>
<p><strong>Service</strong> refers to the Application.</p>
</li>
<li>
<p><strong>You</strong> means the individual accessing the Service, or the company, or other legal entity on behalf of which such individual is accessing or using the Service, as applicable.</p>
</li>
<li>
<p><strong>Application</strong> means the software program provided by the Company downloaded by You on any electronic device named Test proxy generator.</p>
</li>
</ul>
<h2>Disclaimer</h2>
<p>The information contained on the Service is for general information purposes only.</p>
<p>The Company assumes no responsibility for errors or omissions in the contents of the Service.</p>
<p>In no event shall the Company be liable for any special, direct, indirect, consequential, or incidental damages or any damages whatsoever, whether in an action of contract, negligence or other tort, arising out of or in connection with the use of the Service or the contents of the Service. The Company reserves the right to make additions, deletions, or modifications to the contents on the Service at any time without prior notice.</a>.</p>
<p>The Company does not warrant that the Service is free of viruses or other harmful components.</p>
<h2>External Links Disclaimer</h2>
<p>The Service may contain links to external websites that are not provided or maintained by or in any way affiliated with the Company.</p>
<p>Please note that the Company does not guarantee the accuracy, relevance, timeliness, or completeness of any information on these external websites.</p>
<h2>Errors and Omissions Disclaimer</h2>
<p>The information given by the Service is for general guidance on matters of interest only. Even if the Company takes every precaution to ensure that the content of the Service is both current and accurate, errors can occur. Plus, given the changing nature of laws, rules and regulations, there may be delays, omissions or inaccuracies in the information contained on the Service.</p>
<p>The Company is not responsible for any errors or omissions, or for the results obtained from the use of this information.</p>
<h2>Fair Use Disclaimer</h2>
<p>The Company may use copyrighted material which has not always been specifically authorized by the copyright owner. The Company is making such material available for criticism, comment, news reporting, teaching, scholarship, or research.</p>
<p>The Company believes this constitutes a &quot;fair use&quot; of any such copyrighted material as provided for in section 107 of the United States Copyright law.</p>
<p>If You wish to use copyrighted material from the Service for your own purposes that go beyond fair use, You must obtain permission from the copyright owner.</p>
<h2>Views Expressed Disclaimer</h2>
<p>The Service may contain views and opinions which are those of the authors and do not necessarily reflect the official policy or position of any other author, agency, organization, employer or company, including the Company.</p>
<p>Comments published by users are their sole responsibility and the users will take full responsibility, liability and blame for any libel or litigation that results from something written in or as a direct result of something written in a comment. The Company is not liable for any comment published by users and reserves the right to delete any comment for any reason whatsoever.</p>
<h2>No Responsibility Disclaimer</h2>
<p>The information on the Service is provided with the understanding that the Company is not herein engaged in rendering legal, accounting, tax, or other professional advice and services. As such, it should not be used as a substitute for consultation with professional accounting, tax, legal or other competent advisers.</p>
<p>In no event shall the Company or its suppliers be liable for any special, incidental, indirect, or consequential damages whatsoever arising out of or in connection with your access or use or inability to access or use the Service.</p>
<h2>&quot;Use at Your Own Risk&quot; Disclaimer</h2>
<p>All information in the Service is provided &quot;as is&quot;, with no guarantee of completeness, accuracy, timeliness or of the results obtained from the use of this information, and without warranty of any kind, express or implied, including, but not limited to warranties of performance, merchantability and fitness for a particular purpose.</p>
<p>The Company will not be liable to You or anyone else for any decision made or action taken in reliance on the information given by the Service or for any consequential, special or similar damages, even if advised of the possibility of such damages.</p>
<h2>Contact Us</h2>
<p>If you have any questions about this Disclaimer, You can contact Us:</p>
<ul>
<li>By visiting this page on our website: <a href="https://github.com/Inject0r77" rel="external nofollow noopener" target="_blank">https://github.com/Inject0r77</a></li>
</ul>
