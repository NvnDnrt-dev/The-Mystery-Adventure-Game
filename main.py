import time
import os

# Color codes untuk terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_story(text, delay=0.03):
    """Print text dengan efek typing"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_choice(choices):
    """Print pilihan dengan format yang rapi"""
    print(f"\n{Colors.YELLOW}Pilihan Anda:{Colors.ENDC}")
    for key, value in choices.items():
        print(f"{Colors.CYAN}{key}. {value}{Colors.ENDC}")

def get_valid_choice(choices):
    """Dapatkan input yang valid dari pemain"""
    while True:
        pilihan = input(f"\n{Colors.BOLD}Masukkan pilihan Anda ({'/'.join(map(str, choices.keys()))}): {Colors.ENDC}").strip()
        if pilihan in choices:
            return pilihan
        print(f"{Colors.RED}Pilihan tidak valid! Coba lagi.{Colors.ENDC}")

def intro():
    """Pengenalan game"""
    clear_screen()
    print(f"{Colors.HEADER}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}║   LIAR'S GAMBIT: The Underground Game  ║{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}║     Terinspirasi dari Manga: USOGUI    ║{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    time.sleep(1)
    print_story("Selamat datang di dunia gelap perjudian dan penipuan...", delay=0.02)
    time.sleep(2)

def chapter_1(nama):
    """Chapter 1: Perkenalan di Underground Casino"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 1: Undangan Misterius ==={Colors.ENDC}\n")
    
    print_story(f"Malam hari yang gelap. {nama} bermain di kasino bawah tanah yang tersembunyi di pusat kota.")
    time.sleep(1)
    print_story("Anda baru saja menang besar di permainan poker, tetapi...")
    time.sleep(1)
    print_story("Seorang pria misterius mendekat dengan senyum mencolok.\n")
    time.sleep(1)
    
    print_story("???     : 'Wah, pemain baru yang menarik. Nama saya Kiji. Aku punya proposisi untuk Anda.'")
    time.sleep(2)
    print_story("Kiji    : 'Ada turnamen rahasia minggu depan. Hadiah utamanya bukan hanya uang...'\n")
    time.sleep(2)
    
    print_choice({
        "1": "Dengarkan PropForward Kiji dengan penuh minat",
        "2": "Tolak dan pergi dari kasino",
        "3": "Coba membaca ekspresi Kiji untuk mendeteksi kebohongan"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return chapter_2_eager(nama)
    elif pilihan == "2":
        return bad_ending_scaredy(nama)
    elif pilihan == "3":
        return chapter_2_detective(nama)

def chapter_2_eager(nama):
    """Chapter 2: Jalur Antusias"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 2: The Mysterious Game ==={Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Aku tertarik. Ceritakan lebih detail.'")
    time.sleep(1)
    print_story("Kiji    : 'Turnamen tiga hari. Peserta terpilih. Permainan berbeda setiap hari.'")
    time.sleep(1)
    print_story("Kiji    : 'Tidak hanya keberuntungan... tapi juga kemampuan membaca manusia yang dibutuhkan.'\n")
    time.sleep(1)
    
    print_story("Dia mengeluarkan kartu undangan mewah dari sakunya.")
    time.sleep(1)
    print_story("Kiji    : 'Keputusan ada di tanganmu. Menerima atau tidak?'\n")
    time.sleep(1)
    
    print_choice({
        "1": "Terima undangan! Anda ingin menjadi yang terbaik",
        "2": "Minta waktu untuk berpikir",
        "3": "Tanya tentang hadiah sebenarnya"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return chapter_3_bold(nama)
    elif pilihan == "2":
        return neutral_ending_late(nama)
    elif pilihan == "3":
        return chapter_3_curious(nama)

def chapter_2_detective(nama):
    """Chapter 2: Jalur Detektif"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 2: The Perceptive Path ==={Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Kamu terlihat terlalu percaya diri. Ada yang kamu sembunyikan.'")
    time.sleep(1)
    print_story("Kiji mengerutkan alis. Matanya berkilau...")
    time.sleep(1)
    print_story("Kiji    : 'Menarik. Sudah lama tidak bertemu orang yang bisa membaca aku.'")
    time.sleep(1)
    print_story("Kiji    : 'Benar. Ada yang aku sembunyikan. Tapi bukan ancaman. Ini... kesempatan.'\n")
    time.sleep(1)
    
    print_story("Dia memberikan dua pilihan dengan jari menunjuk:")
    time.sleep(1)
    print_story("Kiji    : 'Jalur mudah: Ikuti instruksiku tanpa bertanya.'")
    time.sleep(1)
    print_story("Kiji    : 'Jalur berbahaya: Mainkan melawanku dulu untuk buktikan kemampuanmu.'\n")
    time.sleep(1)
    
    print_choice({
        "1": "Pilih jalur mudah - ikuti instruksinya",
        "2": "Tantang Kiji untuk bermain sekarang",
        "3": "Minta bukti bahwa ini bukan jebakan"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return neutral_ending_puppet(nama)
    elif pilihan == "2":
        return chapter_3_challenge(nama)
    elif pilihan == "3":
        return true_ending_prepare(nama)

def chapter_3_bold(nama):
    """Chapter 3: Jalur Berani"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 3: The Tournament Begins ==={Colors.ENDC}\n")
    
    print_story("Tiga hari kemudian, di warehouse rahasia...")
    time.sleep(1)
    print_story(f"{nama} dan 7 peserta lain berkumpul di ruangan tertutup.")
    time.sleep(1)
    print_story("Kiji berdiri di depan dengan senyum misterius.")
    time.sleep(1)
    print_story("Kiji    : 'Hari pertama: Permainan Liar (Mendeteksi Kebohongan)'")
    time.sleep(1)
    print_story("Kiji    : 'Siapa yang tertangkap berbohong akan kehilangan 50 juta yen.'\n")
    time.sleep(2)
    
    print_story("Permainan dimulai. Semua orang membuat pernyataan tentang diri mereka.")
    time.sleep(1)
    print_story("Kiji menunjuk pada seorang wanita berambut merah.")
    time.sleep(1)
    print_story("Kiji    : 'Kamu berbohong. Akui sekarang.'\n")
    time.sleep(1)
    
    print_story("Kemudian Kiji menunjuk ke arahmu.")
    time.sleep(1)
    print_story("Kiji    : 'Saatnya kamu memberikan pernyataan sejati tentang dirimu.'\n")
    time.sleep(1)
    
    print_choice({
        "1": "Buat pernyataan jujur - tidak ada yang perlu disembunyikan",
        "2": "Buat pernyataan palsu yang sangat meyakinkan",
        "3": "Berakting serius lalu mengungkap kebenaran di akhir"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return bad_ending_predictable(nama)
    elif pilihan == "2":
        return chapter_4_deceit(nama)
    elif pilihan == "3":
        return chapter_4_strategy(nama)

def chapter_3_curious(nama):
    """Chapter 3: Jalur Penasaran"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 3: Hidden Truth ==={Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Apa hadiah sebenarnya? Uang tidak pernah cukup untuk turnamen seperti ini.'")
    time.sleep(1)
    print_story("Kiji tertawa dengan cara yang mengganggu.")
    time.sleep(1)
    print_story("Kiji    : 'Pandai! Hadiah utamanya adalah... kesuksesan finansial seumur hidup.'")
    time.sleep(1)
    print_story("Kiji    : 'Tapi ada syarat: Pemenang harus bekerja untukku.'")
    time.sleep(1)
    print_story("Kiji    : 'Melawan lawan-lawan terberat di dunia underground.'")
    time.sleep(1)
    print_story("Kiji    : 'Bersiaplah untuk malam yang tidak akan pernah kamu lupakan.'\n")
    time.sleep(2)
    
    print_story("Tiga hari kemudian, turnamen dimulai dengan intrik yang belum pernah terjadi...")
    time.sleep(1)
    print_choice({
        "1": "Main dengan strategi defensif - hindari risiko tinggi",
        "2": "Main agresif - dominasi semua pesaing",
        "3": "Bentuk aliansi dengan pesaing lain"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return neutral_ending_survivor(nama)
    elif pilihan == "2":
        return chapter_4_domination(nama)
    elif pilihan == "3":
        return chapter_4_alliance(nama)

def chapter_3_challenge(nama):
    """Chapter 3: Jalur Tantangan"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 3: One-on-One Duel ==={Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Baik. Mainkan dengan aku sekarang. Buktikan bahwa aku layak.'")
    time.sleep(1)
    print_story("Kiji tersenyum puas.")
    time.sleep(1)
    print_story("Kiji    : 'Permainan Poker. Satu putaran. Semua atau tidak sama sekali.'")
    time.sleep(2)
    
    print_story("Mereka duduk di meja. Kartu dibagikan...")
    time.sleep(1)
    print_story("Tangan Anda: Ace-King of Hearts (Kombinasi kuat)")
    time.sleep(1)
    print_story("Pot telah mencapai 100 juta yen.\n")
    time.sleep(1)
    
    print_story("Kiji memandangmu dengan mata yang tajam.")
    time.sleep(1)
    print_story("Kiji    : 'Sekarang aku all-in.'\n")
    time.sleep(1)
    
    print_choice({
        "1": "Fold - bertahan dan tunggu kesempatan lain",
        "2": "Call - percaya pada kartu Anda",
        "3": "Raise - pertaruhan lebih besar lagi"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return neutral_ending_coward(nama)
    elif pilihan == "2":
        return chapter_4_final_duel(nama)
    elif pilihan == "3":
        return bad_ending_overconfident(nama)

def chapter_4_deceit(nama):
    """Chapter 4: Jalur Penipuan"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 4: The Art of Deception ==={Colors.ENDC}\n")
    
    print_story(f"{nama}  : (Dengan percaya diri) 'Aku seorang detektif privat yang melacak criminal.'")
    print_story("(Pernyataan bohong - sebenarnya kamu hanya seorang office worker biasa)\n")
    time.sleep(1)
    
    print_story("Kiji menatapmu dengan seksama. Tensial meningkat...")
    time.sleep(1)
    print_story("Kiji    : 'Lanjut ke putaran berikutnya!'")
    time.sleep(1)
    print_story("Peserta lain berbisik - 'Dia lolos!'")
    time.sleep(2)
    
    print_story("Hari kedua dan ketiga berlalu dengan tantangan yang semakin berat.")
    time.sleep(1)
    print_story("Dengan manipulasi dan kontrol emosi, Anda lolos ke final.\n")
    time.sleep(1)
    
    print_choice({
        "1": "Hadapi Kiji di final dengan taktik yang sama",
        "2": "Ubah taktik - tunjukkan kartu sejatimu",
        "3": "Curi catatan Kiji sebelum final"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return bad_ending_exposed(nama)
    elif pilihan == "2":
        return true_ending_mutual_respect(nama)
    elif pilihan == "3":
        return bad_ending_caught(nama)

def chapter_4_strategy(nama):
    """Chapter 4: Jalur Strategis"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 4: The Strategic Master ==={Colors.ENDC}\n")
    
    print_story(f"{nama}  : (Dengan serius) 'Aku tidak takut kalah, tapi aku juga tidak bodoh.'")
    print_story("'Permainan ini dirancang untuk mengeliminasi yang lemah. Aku akan bertahan.'")
    time.sleep(1)
    print_story("(Anda memberikan gambaran yang ambigu - benar tapi tidak sepenuhnya terbuka)\n")
    time.sleep(2)
    
    print_story("Ronde demi ronde berlalu.")
    time.sleep(1)
    print_story("Anda bermain dengan hati-hati, mempelajari taktik setiap lawan.")
    time.sleep(1)
    print_story("Peserta yang tidak ada lagi gugur satu per satu.\n")
    time.sleep(1)
    
    print_story("Final tiba. Hanya tersisa Anda dan seorang wanita misterius bernama Luna.")
    time.sleep(1)
    print_story("Luna    : 'Aku tahu siapa kamu sebenarnya.'")
    time.sleep(1)
    print_story("Luna    : 'Pertanyaannya: Apakah kamu akan mengakui atau mempertahankan rahasia?'\n")
    time.sleep(1)
    
    print_choice({
        "1": "Akui identitas sebenarmu - jadilah jujur",
        "2": "Pertahankan misteri - tetap tersembunyi",
        "3": "Ajak Luna untuk berkolaborasi melawan Kiji"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return true_ending_honest_path(nama)
    elif pilihan == "2":
        return neutral_ending_mysterious(nama)
    elif pilihan == "3":
        return chapter_4_alliance_endgame(nama)

def chapter_4_domination(nama):
    """Chapter 4: Jalur Dominasi"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 4: Overwhelming Power ==={Colors.ENDC}\n")
    
    print_story("Dengan strategi agresif, Anda menghancurkan setiap lawan yang ada.")
    time.sleep(1)
    print_story("Peserta satu demi satu gugur di bawah tekanan psikologis Anda.")
    time.sleep(1)
    print_story("Kiji mengamati dengan ekspresi yang semakin serius.\n")
    time.sleep(1)
    
    print_story(f"{nama} lolos ke putaran final dengan kemenangan telak.")
    time.sleep(1)
    print_story("Saat final dimulai, Kiji bangkit dari tempat duduknya.\n")
    time.sleep(1)
    
    print_story("Kiji    : 'Kamu benar-benar luar biasa.'")
    time.sleep(1)
    print_story("Kiji    : 'Tapi ada satu hal yang tidak kamu pahami...'")
    time.sleep(1)
    print_story("Kiji    : 'Permainan ini tidak pernah tentang siapa yang terkuat.'")
    time.sleep(1)
    print_story("Kiji    : 'Ini tentang siapa yang paling bijaksana.'\n")
    time.sleep(2)
    
    print_choice({
        "1": "Abaikan kata-kata Kiji dan mainkan kartu terakhir",
        "2": "Dengarkan Kiji dan tanyakan maksudnya",
        "3": "Serang Kiji sekarang sebelum dia mengaktifkan jebakan apapun"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return bad_ending_trap(nama)
    elif pilihan == "2":
        return true_ending_enlightenment(nama)
    elif pilihan == "3":
        return bad_ending_violent(nama)

def chapter_4_alliance(nama):
    """Chapter 4: Jalur Aliansi"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 4: United Front ==={Colors.ENDC}\n")
    
    print_story("Dengan membentuk aliansi, Anda dan pesaing lain bekerja sama.")
    time.sleep(1)
    print_story("Ronde demi ronde, kalian mengecek taktik satu sama lain.")
    time.sleep(1)
    print_story("Kiji menyadari ada sesuatu yang berbeda.\n")
    time.sleep(1)
    
    print_story("Kecurangan? Tidak. Kerja sama strategis? Mungkin.")
    time.sleep(1)
    print_story("Menjelang final, ketua dewan undian menjadi khawatir.\n")
    time.sleep(1)
    
    print_story("Ketua    : 'Permainan ini dirancang untuk individu, bukan kelompok!'")
    time.sleep(1)
    print_story("Kiji    : (Tertawa) 'Tidak masalah. Mari kita lihat siapa yang paling cemerlang.'\n")
    time.sleep(1)
    
    print_choice({
        "1": "Bubarkan aliansi dan mainkan solo di final",
        "2": "Pertahankan aliansi dan hadapi konsekuensinya",
        "3": "Khianati teman aliansi untuk menang sendirian"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return neutral_ending_alone_again(nama)
    elif pilihan == "2":
        return true_ending_loyal_victory(nama)
    elif pilihan == "3":
        return bad_ending_betrayal(nama)

def chapter_4_final_duel(nama):
    """Chapter 4: Duel Final Melawan Kiji"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 4: Final Face-Off ==={Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Aku Call. Tunjukkan kartumu.'")
    time.sleep(1)
    print_story("\nKiji membuka kartu lambat-lambat...")
    time.sleep(1)
    print_story("Kiji    : Ace-King of Spades. (Full House)")
    time.sleep(1)
    print_story("\nMatamu membesar. Itu kombinasi lebih kuat!")
    time.sleep(1)
    print_story("Tapi...")
    time.sleep(2)
    
    print_story("Kiji    : 'Tunggu. Ada sampai lima kartu dunia.'")
    time.sleep(1)
    print_story("(Dengan santai...) Kiji menunjukkan dompetnya di atas meja.")
    time.sleep(1)
    print_story("'Sebenarnya, aku sudah tahu kamu akan call.'")
    time.sleep(1)
    print_story("'Aku sudah tahu karena aku MEMBACA KAMU.'\n")
    time.sleep(2)
    
    print_choice({
        "1": "Akui kekalahan dengan hormat",
        "2": "Gugat permainan ini tidak fair",
        "3": "Terima tawaran Kiji untuk bekerja bersamanya"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return true_ending_apprentice(nama)
    elif pilihan == "2":
        return bad_ending_sore_loser(nama)
    elif pilihan == "3":
        return true_ending_partnership(nama)

# ============ JALUR CERITA TAMBAHAN ============

def chapter_4_alliance_endgame(nama):
    """Chapter 4: Akhir Aliansi"""
    clear_screen()
    print(f"{Colors.BLUE}{Colors.BOLD}=== CHAPTER 4: Breaking Point ==={Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Luna, aku tahu kita bisa mengalahkan Kiji jika bersama.'")
    time.sleep(1)
    print_story("Luna    : 'Kamu berpikir itu strategi yang bagus? Kiji sudah mengantisipasi ini.'")
    time.sleep(1)
    print_story("Luna mengeluarkan catatan dari saku.",)
    time.sleep(1)
    print_story("Luna    : 'Dia menyuruhku untuk mengatakannya. Dia ingin melihat apa yang akan kamu lakukan.'\n")
    time.sleep(2)
    
    print_choice({
        "1": "Percayai Luna dan lanjutkan rencana",
        "2": "Percayai insting - Luna adalah spy Kiji",
        "3": "Ambil catatan dan baca sendiri"
    })
    
    pilihan = get_valid_choice({"1": "", "2": "", "3": ""})
    
    if pilihan == "1":
        return true_ending_ultimate_victory(nama)
    elif pilihan == "2":
        return chapter_4_final_duel(nama)
    elif pilihan == "3":
        return neutral_ending_knowledge(nama)

# ============ ENDING CERITA ============

def true_ending_prepare(nama):
    """TRUE ENDING: Persiapan Matang"""
    clear_screen()
    print(f"{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║         ★ TRUE ENDING ★                ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║      The Prepared Strategist           ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Jika ini serius, aku perlu bukti nyata tentang organisasimu.'")
    time.sleep(1)
    print_story("Kiji tersenyum senang - senyum pertama yang terlihat tulus.")
    time.sleep(1)
    print_story("Kiji    : 'Akhirnya! Seseorang yang tidak mudah tertipu.'")
    time.sleep(1)
    print_story("Kiji    : 'Baik, aku akan batukkan kebenaran sepenuhnya.'\n")
    time.sleep(2)
    
    print_story("Kiji menjelaskan sebuah organisasi bawah tanah yang membantu para pemain")
    print_story("mencapai kehidupan finansial ideal dengan menggunakan kecerdasan dan strategi.")
    time.sleep(2)
    
    print_story(f"{nama} waktu dua minggu untuk mempersiapkan. Riset, latihan, strategi.")
    time.sleep(1)
    print_story("Saat turnamen tiba, Anda masuk dengan pemahaman penuh dan percaya diri.\n")
    time.sleep(1)
    
    print_story("Hasilnya? KEMENANGAN SPEKTAKULER!")
    time.sleep(1)
    print_story("Anda mengalahkan semua pesaing dengan kecerdasan dan perencanaan.")
    time.sleep(1)
    print_story("Kiji merekrutmu sebagai mitra untuk misi-misi selanjutnya.\n")
    time.sleep(2)
    
    print_story("Anda memahami: Dalam permainan kehidupan, bersiap dengan matang adalah kunci.")
    time.sleep(1)
    print_story("Bukan hanya keberuntungan atau kecerdasan bawaan.")
    time.sleep(1)
    print_story("Tapi dedikasi, penelitian, dan strategi jangka panjang.\n")
    time.sleep(2)
    print(f"{Colors.GREEN}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING SEJATI TERCAPAI]{Colors.ENDC}\n")

def true_ending_mutual_respect(nama):
    """TRUE ENDING: Saling Menghormati"""
    clear_screen()
    print(f"{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║         ★ TRUE ENDING ★                ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║      The Respectful Opponent           ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Di putaran final, ")
    print_story(f"{nama} menghadapi Kiji dengan tulus.")
    time.sleep(1)
    print_story(f"{nama}  : 'Aku bermain dengan semua kemampuanku. Mari kita lihat siapa yang lebih baik.'")
    time.sleep(1)
    print_story("Pertandingan terakhir berlangsung seru dan ketat.")
    time.sleep(1)
    print_story("Pada akhirnya, kedua belah pihak bertemu di puncak kemampuan mereka.\n")
    time.sleep(2)
    
    print_story("Kiji berdiri dan memberikan hormat kepada Anda.")
    time.sleep(1)
    print_story("Kiji    : 'Aku melihat diri sendiri dalam dirimu. Pemain sejati.'")
    time.sleep(1)
    print_story("Kiji    : 'Yang penting dalam kehidupan bukan siapa yang menang atau kalah.'")
    time.sleep(1)
    print_story("Kiji    : 'Tapi bagaimana kita bermain. Dengan hormat dan integritas.'\n")
    time.sleep(2)
    
    print_story("Anda menang. Hadiah besar dalam tas emas.")
    time.sleep(1)
    print_story("Tapi yang lebih berharga adalah pengetahuan:")
    time.sleep(1)
    print_story("Kepercayaan diri sejati datang dari bermain dengan jujur, bukan dari tipu-tipu.\n")
    time.sleep(2)
    print(f"{Colors.GREEN}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING SEJATI TERCAPAI]{Colors.ENDC}\n")

def true_ending_honest_path(nama):
    """TRUE ENDING: Jalan Kejujuran"""
    clear_screen()
    print(f"{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║         ★ TRUE ENDING ★                ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║      The Honest Victor                 ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Aku adalah seorang office worker biasa yang bermimpi lebih.'")
    time.sleep(1)
    print_story("'Tidak ada yang istimewa tentang diriku kecuali keinginan untuk belajar.'")
    time.sleep(1)
    print_story("Luna tersenyum.")
    time.sleep(1)
    print_story("Luna    : 'Itu yang ingin aku dengar. Seseorang yang jujur tentang awalnya.'\n")
    time.sleep(2)
    
    print_story("Dalam final, kedua pemain bermain dengan kejujuran.")
    time.sleep(1)
    print_story("Anda menang karena kemampuan, bukan tipuan.")
    time.sleep(1)
    print_story("Kiji melihat ini dan tersenyum puas.")
    time.sleep(1)
    print_story("Kiji    : 'Inilah yang saya cari. Pemenang sejati.'\n")
    time.sleep(2)
    
    print_story("Hadiah menjadi milik Anda.")
    time.sleep(1)
    print_story("Lebih penting lagi, Anda mendapatkan posisi sebagai partner Kiji dalam organisasi.")
    time.sleep(1)
    print_story("Karir bermula dari kejujuran dan integritas pribadi.\n")
    time.sleep(2)
    print(f"{Colors.GREEN}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING SEJATI TERCAPAI]{Colors.ENDC}\n")

def true_ending_enlightenment(nama):
    """TRUE ENDING: Pencerahan"""
    clear_screen()
    print(f"{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║         ★ TRUE ENDING ★                ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║      The Enlightened Champion          ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Jelaskan. Apa yang ingin kamu ajarkan padaku?'")
    time.sleep(1)
    print_story("Kiji duduk dan mulai berbicara selama berjam-jam.")
    time.sleep(1)
    print_story("Dia mengungkap filosofi hidup yang mendalam tentang kekuatan pikiran.")
    time.sleep(1)
    print_story("Tentang bagaimana kecerdasan emosional lebih penting dari kekuatan.")
    time.sleep(1)
    print_story("Tentang bagaimana memenangkan permainan tidak penting")
    print_story("jika Anda kehilangan diri sendiri dalam prosesnya.\n")
    time.sleep(2)
    
    print_story("Saat final tiba, Anda memahami sesuatu yang fundamental.")
    time.sleep(1)
    print_story("Kemenangan sejati bukan tentang mengalahkan lawan.")
    time.sleep(1)
    print_story("Tetapi tentang menguasai diri sendiri.\n")
    time.sleep(1)
    
    print_story("Dengan pencerahan ini, Anda bermain dengan sempurna.")
    time.sleep(1)
    print_story("Kiji kalah dengan murah hati.")
    time.sleep(1)
    print_story("Kiji    : 'Kamu adalah siswa terbaik yang pernah aku miliki.'\n")
    time.sleep(2)
    
    print_story("Hadiah adalah kekayaan. Tapi pencerahan adalah perbendaharaan sesungguhnya.")
    time.sleep(2)
    print(f"{Colors.GREEN}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING SEJATI TERCAPAI]{Colors.ENDC}\n")

def true_ending_loyal_victory(nama):
    """TRUE ENDING: Kemenangan Loyalitas"""
    clear_screen()
    print(f"{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║         ★ TRUE ENDING ★                ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║      The Loyal Champion               ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Dengan mempertahankan aliansi Anda, Anda menunjukkan karakter sejati.")
    time.sleep(1)
    print_story("Bahwa uang dan kemenangan tidak lebih penting dari loyalitas.")
    time.sleep(1)
    print_story("Kiji menghentikan permainan dan bergerak ke depan.\n")
    time.sleep(2)
    
    print_story("Kiji    : 'Jarang sekali saya menemukan seseorang yang tidak rela mengkhianati.'")
    time.sleep(1)
    print_story("Kiji    : 'Orang seperti itu adalah aset sejati dalam organisasi kami.'\n")
    time.sleep(1)
    
    print_story("Alih-alih pertandingan, Kiji mengundang Anda dan aliansi Anda")
    print_story("untuk bergabung sebagai tim dalam operasi yang lebih besar.")
    time.sleep(2)
    
    print_story("Hadiah finansial berlipat ganda karena kerja sama kelompok.")
    time.sleep(1)
    print_story("Lebih penting lagi, Anda memiliki keluarga besar yang saling mendukung.")
    time.sleep(1)
    print_story("Itulah kemenangan sejati.\n")
    time.sleep(2)
    print(f"{Colors.GREEN}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING SEJATI TERCAPAI]{Colors.ENDC}\n")

def true_ending_apprentice(nama):
    """TRUE ENDING: Murid Kiji"""
    clear_screen()
    print(f"{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║         ★ TRUE ENDING ★                ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║      The Rising Apprentice             ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Aku kalah. Tapi aku ingin belajar darimu.'")
    time.sleep(1)
    print_story("Kiji memberikan tangan untuk mengangkat Anda berdiri.")
    time.sleep(1)
    print_story("Kiji    : 'Itu jawaban terbaik yang bisa kamu berikan.'")
    time.sleep(1)
    print_story("Kiji    : 'Orang-orang terbaik bukan yang tidak pernah kalah.'")
    time.sleep(1)
    print_story("Kiji    : 'Tapi orang yang belajar dari kegagalan.'\n")
    time.sleep(2)
    
    print_story("Anda menerima posisi sebagai murid pribadi Kiji.")
    time.sleep(1)
    print_story("Selama tiga tahun ke depan, Anda mempelajari seni membaca manusia,")
    print_story("strategi permainan tingkat lanjut, dan filosofi kehidupan yang mendalam.")
    time.sleep(2)
    
    print_story("Pada akhirnya, Anda menjadi pemain legendaris dalam dunia underground.")
    time.sleep(1)
    print_story("Dengan mentor seperti Kiji, kesuksesan bukan lagi mimpi.\n")
    time.sleep(2)
    print(f"{Colors.GREEN}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING SEJATI TERCAPAI]{Colors.ENDC}\n")

def true_ending_partnership(nama):
    """TRUE ENDING: Kemitraan"""
    clear_screen()
    print(f"{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║         ★ TRUE ENDING ★                ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║      The Perfect Partnership           ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Kunci yang sebenarnya, bukankah kamu sudah tahu aku akan accept?'")
    time.sleep(1)
    print_story("Kiji tertawa - gelak tawa yang tulus dan dalam.")
    time.sleep(1)
    print_story("Kiji    : 'Ya. Dari saat pertama kali aku melihatmu.'")
    time.sleep(1)
    print_story("Kiji    : 'Permainan ini adalah tes. Anda lulus dengan sempurna.'\n")
    time.sleep(2)
    
    print_story("Anda ditawari posisi senioritas dalam organisasi.")
    time.sleep(1)
    print_story("Bukan sebagai karyawan, tetapi sebagai mitra setara dengan Kiji.")
    time.sleep(1)
    print_story("Bersama-sama, kalian membangun jaringan bisnis yang memengaruhi dunia.\n")
    time.sleep(2)
    
    print_story("Tahun-tahun berlalu.")
    time.sleep(1)
    print_story("Dari pemain ground zero, Anda menjadi legenda.")
    time.sleep(1)
    print_story("Dan semua dimulai dari keputusan untuk menerima tangan yang ditawarkan Kiji.\n")
    time.sleep(2)
    print(f"{Colors.GREEN}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING SEJATI TERCAPAI]{Colors.ENDC}\n")

def true_ending_ultimate_victory(nama):
    """TRUE ENDING: Kemenangan Tertinggi"""
    clear_screen()
    print(f"{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║         ★ TRUE ENDING ★                ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║      The Ultimate Gambler              ║{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Anda percayai Luna dan melanjutkan rencana.")
    time.sleep(1)
    print_story("Bersama-sama, dalam putaran final yang spektakuler,")
    print_story("Anda dan Luna melampaui bahkan harapan Kiji sendiri.\n")
    time.sleep(2)
    
    print_story("Strategi yang digabung, intuisi yang sinkron, taktik yang sempurna.")
    time.sleep(1)
    print_story("Bahkan Kiji harus mengakui kekalahan.")
    time.sleep(1)
    print_story("Kiji    : 'Luar biasa. Kalian adalah pemain terbaik yang pernah aku lihat.'\n")
    time.sleep(2)
    
    print_story("Hadiah dibagi bersama Luna. Tapi lebih penting:")
    print_story("Kiji menawarkan kedua-duanya untuk membangun organisasi BARU")
    print_story("yang lebih besar, lebih kuat, dan lebih bermakna.\n")
    time.sleep(2)
    
    print_story("Ini adalah awal dari era baru. Era di mana Anda bukan hanya pemain")
    print_story("tetapi penciptanya sendiri dari masa depan.\n")
    time.sleep(2)
    print(f"{Colors.GREEN}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING SEJATI TERCAPAI]{Colors.ENDC}\n")

# ============ BAD ENDINGS ============

def bad_ending_scaredy(nama):
    """BAD ENDING: Penakut"""
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║         ✗ BAD ENDING ✗                 ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║      The Coward's Regret               ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Tidak. Aku tidak tertarik.'")
    time.sleep(1)
    print_story("Anda pergi dari kasino dan kembali ke kehidupan biasa.")
    time.sleep(1)
    print_story("Bert bertahun-tahun, Anda sering bertanya:")
    time.sleep(1)
    print_story("'Bagaimana jika aku menerima undangan itu?'\n")
    time.sleep(2)
    
    print_story("Kiji pernah menceritakan kepada orang lain tentang pemain yang menolak.")
    time.sleep(1)
    print_story("Dia menjadi legenda yang hilang dari dunia underground.")
    time.sleep(1)
    print_story("Anda tidak pernah tahu kesempatan emas apa yang telah Anda sia-siakan.\n")
    time.sleep(2)
    print(f"{Colors.RED}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING BURUK TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.RED}Pelajaran: Kadang kesempatan hanya datang sekali.{Colors.ENDC}\n")

def bad_ending_predictable(nama):
    """BAD ENDING: Terlalu Mudah Diprediksi"""
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║         ✗ BAD ENDING ✗                 ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║      The Predictable Player            ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Saat Anda memberikan pernyataan jujur,")
    print_story("Kiji langsung tersenyum dengan cara yang sangat berbeda.\n")
    time.sleep(1)
    
    print_story("Kiji    : 'Kamu tahu apa masalahmu?'")
    time.sleep(1)
    print_story("Kiji    : 'Kamu terlalu jujur. Terlalu mudah dibaca.'")
    time.sleep(1)
    print_story("Kiji    : 'Seseorang di level kami tidak bisa bertahan dengan keterbukaan seperti itu.'\n")
    time.sleep(2)
    
    print_story("Anda dieliminasi di putaran pertama.")
    time.sleep(1)
    print_story("Ujaran terakhir Kiji:")
    time.sleep(1)
    print_story("Kiji    : 'Selamat tinggal. Semoga kau belajar untuk tersembunyi lebih baik.'\n")
    time.sleep(2)
    print(f"{Colors.RED}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING BURUK TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.RED}Pelajaran: Di dunia permainan, keterbukaan sepenuhnya adalah kelemahan.{Colors.ENDC}\n")

def bad_ending_exposed(nama):
    """BAD ENDING: Terbongkar"""
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║         ✗ BAD ENDING ✗                 ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║      The Exposed Liar                  ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Di final, Anda menghadapi Kiji dengan taktik penipuan yang sama.")
    time.sleep(1)
    print_story("Tetapi Kiji sudah menonton Anda selama tiga hari penuh.")
    time.sleep(1)
    print_story("Dia tahu setiap gerakan, setiap tatapan, setiap tipu muslihat.\n")
    time.sleep(2)
    
    print_story("Saat Anda mencoba menggertak, Kiji tertawa keras.")
    time.sleep(1)
    print_story("Kiji    : 'Permainanmu sudah aku ketahui sejak putaran kedua.'")
    time.sleep(1)
    print_story("Kiji    : 'Menunggu final hanya untuk mengecewakan harapanmu.'\n")
    time.sleep(2)
    
    print_story("Anda dikalahkan dengan cara yang sangat memalukan.")
    time.sleep(1)
    print_story("Semua pesaing menertawakan Anda.")
    time.sleep(1)
    print_story("Nama Anda menjadi lelucon di dunia underground gambling.\n")
    time.sleep(2)
    print(f"{Colors.RED}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING BURUK TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.RED}Pelajaran: Mereka yang hanya mengandalkan tipu muslihat selalu tertangkap.{Colors.ENDC}\n")

def bad_ending_caught(nama):
    """BAD ENDING: Tertangkap Mencuri"""
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║         ✗ BAD ENDING ✗                 ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║      The Caught Thief                  ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Saat Anda mencoba mencuri catatan Kiji,")
    print_story("Anda langsung tertangkap oleh pengamanan di ruangan.")
    time.sleep(1)
    print_story("Kiji menunggu Anda dengan ekspresi sangat kecewa.\n")
    time.sleep(2)
    
    print_story("Kiji    : 'Ada cara untuk naik ke puncak. Tidak ada cara untuk turun dengan selamat.'")
    time.sleep(1)
    print_story("Anda tidak pernah meninggalkan warehouse itu.")
    time.sleep(1)
    print_story("Pelajaran Anda: Kejujuran jauh lebih aman daripada pencuri.\n")
    time.sleep(2)
    print(f"{Colors.RED}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING BURUK TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.RED}Pelajaran: Tindakan bodoh membawa konsekuensi yang tidak terduga.{Colors.ENDC}\n")

def bad_ending_trap(nama):
    """BAD ENDING: Jebakan"""
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║         ✗ BAD ENDING ✗                 ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║      The Fatal Trap                    ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Anda mengabaikan peringatan Kiji dan bermain kartu terakhir dengan agresif.")
    time.sleep(1)
    print_story("Tetapi... itu adalah jebakan.\n")
    time.sleep(2)
    
    print_story("Kiji telah memposisikan permainan sedemikian rupa sehingga")
    print_story("keserakahan Anda akan membuat Anda kalah total.\n")
    time.sleep(1)
    
    print_story("Kiji    : 'Bijaksana adalah mendengarkan. Anda memilih untuk tidak.'")
    time.sleep(1)
    print_story("Anda tidak hanya kehilangan turnamen. Anda juga kehilangan dana pribadi Anda.\n")
    time.sleep(2)
    print(f"{Colors.RED}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING BURUK TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.RED}Pelajaran: Mendengarkan kebijaksanaan orang lain adalah keterampilan penting.{Colors.ENDC}\n")

def bad_ending_overconfident(nama):
    """BAD ENDING: Terlalu Percaya Diri"""
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║         ✗ BAD ENDING ✗                 ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║      The Overconfident Gambler         ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Anda Raise dengan kartu bagus di tangan.")
    time.sleep(1)
    print_story("Tapi Kiji tidak fold. Dia malah menunjukkan kartu yang lebih baik.")
    time.sleep(1)
    print_story("Anda meledak dalam kemarahan dan kehilangan kontrol.\n")
    time.sleep(2)
    
    print_story("Kiji meninggalkan meja dengan tenang.")
    time.sleep(1)
    print_story("Kiji    : 'Mereka yang tidak bisa mengontrol emosi tidak bisa menggurui hidup.'")
    time.sleep(1)
    print_story("Anda dibekuk oleh petugas kasino karena kekerasan.")
    time.sleep(1)
    print_story("Perjalanan Anda berakhir sebelum benar-benar dimulai.\n")
    time.sleep(2)
    print(f"{Colors.RED}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING BURUK TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.RED}Pelajaran: Kontrol emosi adalah aset terpenting dalam permainan apapun.{Colors.ENDC}\n")

def bad_ending_violent(nama):
    """BAD ENDING: Kekerasan"""
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║         ✗ BAD ENDING ✗                 ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║      The Violent Failure               ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Anda kehilangan akal sehat dan menyerang Kiji secara fisik.")
    time.sleep(1)
    print_story("Tetapi Kiji bukanlah lawan yang biasa. Dia segera menempatkan Anda.")
    time.sleep(1)
    print_story("Kemudian dia membuat panggilan.\n")
    time.sleep(2)
    
    print_story("Polisi tiba. Anda ditangkap atas tuduhan serangan.")
    time.sleep(1)
    print_story("Kiji memberikan kesaksian yang tepat dan akurat.")
    time.sleep(1)
    print_story("Anda menghabiskan tiga tahun di penjara.\n")
    time.sleep(2)
    
    print_story("Permainan skala besar Anda selesai sebelum dimulai.\n")
    time.sleep(2)
    print(f"{Colors.RED}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING BURUK TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.RED}Pelajaran: Kekerasan fisik tidak pernah merupakan jawabannya.{Colors.ENDC}\n")

def bad_ending_sore_loser(nama):
    """BAD ENDING: Penggugat Kekalahan"""
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║         ✗ BAD ENDING ✗                 ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║      The Sore Loser                    ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Ini tidak adil! Permainannya rigged!'")
    time.sleep(1)
    print_story("Anda mulai mengajukan keberatan dan menuduh penipuan.")
    time.sleep(1)
    print_story("Kiji tersenyum dingin.\n")
    time.sleep(1)
    
    print_story("Kiji    : 'Orang yang tidak bisa menerima kekalahan bukan pemain sejati.'")
    time.sleep(1)
    print_story("Anda dikeluarkan dari organisasi selamanya.")
    time.sleep(1)
    print_story("Lebih buruk lagi, Anda mendapatkan label 'pengadil pemberi masalah'")
    print_story("yang mengejar Anda selama bertahun-tahun.\n")
    time.sleep(2)
    print(f"{Colors.RED}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING BURUK TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.RED}Pelajaran: Kekalahan adalah bagian dari permainan. Terima dengan hormat.{Colors.ENDC}\n")

def bad_ending_betrayal(nama):
    """BAD ENDING: Pengkhianat"""
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║         ✗ BAD ENDING ✗                 ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║      The Betrayer's Doom               ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Aku akan mengalahkan kalian semua dan mengambil hadiah sendiri!'")
    time.sleep(1)
    print_story("Anda mengkhianati teman aliansi untuk keuntungan pribadi.\n")
    time.sleep(2)
    
    print_story("Anda memang menang permainan. Mendapatkan hadiah besar.")
    time.sleep(1)
    print_story("Tetapi dalam dunia underground, pengkhianat tidak pernah aman.\n")
    time.sleep(1)
    
    print_story("Tahun-tahun kemudian, orang-orang yang Anda khianati menemukan Anda.")
    time.sleep(1)
    print_story("Hadiah uang tidak bernilai apa-apa ketika Anda tidak bisa menikmatinya")
    print_story("sambil bersembunyi selamanya.\n")
    time.sleep(2)
    print(f"{Colors.RED}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING BURUK TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.RED}Pelajaran: Loyalitas adalah mata uang paling berharga di dunia underground.{Colors.ENDC}\n")

# ============ NEUTRAL ENDINGS ============

def neutral_ending_late(nama):
    """NEUTRAL ENDING: Terlambat"""
    clear_screen()
    print(f"{Colors.YELLOW}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      ~ NEUTRAL ENDING ~                ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      The Opportunity Missed            ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story(f"{nama}  : 'Aku perlu waktu untuk berpikir. Hubungi aku nanti.'")
    time.sleep(1)
    print_story("Kiji mengangguk dan memberikan nomor teleponnya.")
    time.sleep(1)
    print_story("Kiji    : 'Aku menunggu tiga hari. Setelah itu, pintu ini akan tertutup.'\n")
    time.sleep(2)
    
    print_story("Anda kembali ke rumah dan berpikir keras selama tiga hari.")
    time.sleep(1)
    print_story("Pada hari keempat, Anda memutuskan untuk menelepon Kiji.")
    time.sleep(1)
    print_story("Tapi... nomor itu tidak lagi aktif.\n")
    time.sleep(1)
    
    print_story("Kiji sudah pergi ke kota lain.")
    time.sleep(1)
    print_story("Undangan tidak akan pernah datang lagi.")
    time.sleep(1)
    print_story("Anda hidup dengan rasa penyesalan: 'Seandainya aku memutuskan lebih cepat...'\n")
    time.sleep(2)
    print(f"{Colors.YELLOW}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING NETRAL TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.YELLOW}Pelajaran: Indikasi adalah musuh dari keputusan yang buruk.{Colors.ENDC}\n")

def neutral_ending_puppet(nama):
    """NEUTRAL ENDING: Boneka"""
    clear_screen()
    print(f"{Colors.YELLOW}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      ~ NEUTRAL ENDING ~                ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      The Puppet Master's Tool          ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Anda memilih untuk mengikuti instruksi Kiji tanpa pertanyaan.")
    time.sleep(1)
    print_story("Tiga hari berikutnya, Anda hanya melakukan apa yang Kiji katakan.")
    time.sleep(1)
    print_story("Tidak ada otonomi. Tidak ada pilihan pribadi.\n")
    time.sleep(2)
    
    print_story("Anda menang tournament dengan mengikuti strategi Kiji dengan sempurna.")
    time.sleep(1)
    print_story("Anda menjadi kaya secara finansial.")
    time.sleep(1)
    print_story("Tetapi Anda merasa kosong. Seperti boneka yang dimainkan.\n")
    time.sleep(2)
    
    print_story("Kiji menawarkan Anda posisi lebih tinggi, tapi dengan syarat:")
    print_story("Anda harus terus mengikuti instruksinya untuk sisa hidup Anda.")
    time.sleep(1)
    print_story("Anda menerima, tetapi dengan hati yang berat.\n")
    time.sleep(2)
    print(f"{Colors.YELLOW}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING NETRAL TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.YELLOW}Pelajaran: Uang tanpa kebebasan hanya adalah penjara emas.{Colors.ENDC}\n")

def neutral_ending_survivor(nama):
    """NEUTRAL ENDING: Penyintas"""
    clear_screen()
    print(f"{Colors.YELLOW}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      ~ NEUTRAL ENDING ~                ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      The Cautious Survivor             ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Anda bermain dengan hati-hati, menghindari risiko tinggi.")
    time.sleep(1)
    print_story("Strategi defensif membuat Anda bertahan lebih lama dari yang diharapkan.")
    time.sleep(1)
    print_story("Tetapi Anda tidak pernah mendominasi seperti pemain lain.\n")
    time.sleep(2)
    
    print_story("Pada putaran semi-final, Anda bertemu Kiji.")
    time.sleep(1)
    print_story("Anda bermain dengan baik, tetapi bijaksana untuk mengekui keunggulannya.")
    time.sleep(1)
    print_story("Anda kalah, tapi dengan hormat.\n")
    time.sleep(2)
    
    print_story("Kiji memberikan 30% dari hadiah utama sebagai tanda penghargaan.")
    time.sleep(1)
    print_story("Anda mendapatkan kesuksesan yang modest, bukan spektakuler.")
    time.sleep(1)
    print_story("Hidup Anda meningkat, tetapi Anda tidak pernah menjadi legenda.\n")
    time.sleep(2)
    print(f"{Colors.YELLOW}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING NETRAL TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.YELLOW}Pelajaran: Bermain aman membuat Anda survive, tapi bukan terkenal.{Colors.ENDC}\n")

def neutral_ending_coward(nama):
    """NEUTRAL ENDING: Pengecut"""
    clear_screen()
    print(f"{Colors.YELLOW}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      ~ NEUTRAL ENDING ~                ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      The Fearful Gambler               ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Anda Fold, memilih keamanan daripada risiko.")
    time.sleep(1)
    print_story("Kiji mengangguk dengan senyum membingungkan.")
    time.sleep(1)
    print_story("Kiji    : 'Pilihan yang bijaksana. Tapi bukan pilihan pemenang.'\n")
    time.sleep(2)
    
    print_story("Kiji melanjutkan pertandingan dengan pemain lain.")
    time.sleep(1)
    print_story("Anda tidak dieliminasi, tetapi Anda juga tidak pernah berkembang.")
    time.sleep(1)
    print_story("Anda tetap menjadi pemain middle-tier yang tidak dikenal.\n")
    time.sleep(2)
    
    print_story("Bertahun-tahun kemudian, Anda menonton dari kejauhan")
    print_story("ketika Kiji membangun empire yang besar.")
    time.sleep(1)
    print_story("Anda masih bermain, tapi sudah terlambat untuk menjadi bagian dari mimpi besar.\n")
    time.sleep(2)
    print(f"{Colors.YELLOW}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING NETRAL TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.YELLOW}Pelajaran: Takut mengambil risiko adalah cara terbaik untuk tersisa biasa saja.{Colors.ENDC}\n")

def neutral_ending_mysterious(nama):
    """NEUTRAL ENDING: Misteri"""
    clear_screen()
    print(f"{Colors.YELLOW}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      ~ NEUTRAL ENDING ~                ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      The Enigma                        ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Anda mempertahankan misteri sepanjang permainan.")
    time.sleep(1)
    print_story("Luna tidak pernah benar-benar mengerti siapa Anda.")
    time.sleep(1)
    print_story("Bahkan Kiji terkesan dan sedikit kebingungan.\n")
    time.sleep(2)
    
    print_story("Anda menang tournament dengan strategi yang misterius.")
    time.sleep(1)
    print_story("Kiji memberikan hadiah dengan catatan:")
    time.sleep(1)
    print_story("Kiji    : 'Seorang pemain yang tidak pernah sepenuhnya terbuka. Saya menghormati itu.'\n")
    time.sleep(2)
    
    print_story("Anda menerima hadiah dan pergi.")
    time.sleep(1)
    print_story("Tidak ada yang benar-benar tahu siapa Anda.")
    time.sleep(1)
    print_story("Anda hidup sebagai legenda tanpa nama dalam dunia underground.\n")
    time.sleep(2)
    print(f"{Colors.YELLOW}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING NETRAL TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.YELLOW}Pelajaran: Kadang menjadi misteri adalah keunggulan terbesar.{Colors.ENDC}\n")

def neutral_ending_alone_again(nama):
    """NEUTRAL ENDING: Sendirian Lagi"""
    clear_screen()
    print(f"{Colors.YELLOW}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      ~ NEUTRAL ENDING ~                ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      Alone Once More                   ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Anda memutuskan untuk bubarkan aliansi sebelum final.")
    time.sleep(1)
    print_story("Teman-teman aliansi merasa dikhianati, meski bukan ancaman fisik.")
    time.sleep(1)
    print_story("Hubungan buruk dengan mereka tetap ada.\n")
    time.sleep(2)
    
    print_story("Di final sendirian, Anda berjuang melawan Kiji.")
    time.sleep(1)
    print_story("Anda kalah dengan sedikit perbedaan.")
    time.sleep(1)
    print_story("Kiji memberikan 40% hadiah sebagai konsolasi.\n")
    time.sleep(2)
    
    print_story("Anda mendapatkan kesuksesan finansial yang layak,")
    print_story("tetapi kehilangan teman dan aliansi yang berharga.")
    time.sleep(1)
    print_story("Sendirian dengan uang bukanlah definisi kemenangan sejati.\n")
    time.sleep(2)
    print(f"{Colors.YELLOW}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING NETRAL TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.YELLOW}Pelajaran: Uang sendiri tidak membawa kebahagiaan tanpa hubungan manusia.{Colors.ENDC}\n")

def neutral_ending_knowledge(nama):
    """NEUTRAL ENDING: Pengetahuan"""
    clear_screen()
    print(f"{Colors.YELLOW}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      ~ NEUTRAL ENDING ~                ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║      The Informed Choice               ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    
    print_story("Anda membaca catatan dan menemukan semuanya.")
    time.sleep(1)
    print_story("Strategi Kiji, kelemahan Luna, jalur tersembunyi menuju kemenangan.")
    time.sleep(1)
    print_story("Dengan pengetahuan ini, Anda bermain dengan sempurna di final.\n")
    time.sleep(2)
    
    print_story("Anda menang. Hadiah adalah milik Anda.")
    time.sleep(1)
    print_story("Tetapi Kiji tidak terkesan.")
    time.sleep(1)
    print_story("Kiji    : 'Kamu menang karena informasi, bukan karena bakat.'")
    time.sleep(1)
    print_story("Kiji    : 'Itu bukan kemenangan sejati dalam buku ku.'\n")
    time.sleep(2)
    
    print_story("Anda kaya, tetapi tidak pernah mendapat pengakuan dari Kiji.")
    time.sleep(1)
    print_story("Uang Anda membeli banyak hal, tapi bukan kebanggaan.\n")
    time.sleep(2)
    print(f"{Colors.YELLOW}{Colors.BOLD}[PERMAINAN BERAKHIR - ENDING NETRAL TERCAPAI]{Colors.ENDC}")
    print(f"{Colors.YELLOW}Pelajaran: Kemenangan yang dicuri oleh informasi tidak pernah memuaskan.{Colors.ENDC}\n")

def game_utama():
    """Fungsi utama permainan"""
    intro()
    nama = input(f"{Colors.BOLD}Siapa namamu? {Colors.ENDC}")
    
    if not nama or nama.strip() == "":
        nama = "Mysterious Gambler"
    
    chapter_1(nama.strip())
    
    print("\n" + "="*42)
    print(f"{Colors.BOLD}Terima kasih telah bermain!{Colors.ENDC}")
    print("="*42)
    print(f"\n{Colors.CYAN}Ingin bermain lagi? Jalankan program ini kembali.{Colors.ENDC}\n")

if __name__ == "__main__":
    try:
        game_utama()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Permainan dihentikan oleh pemain. Sampai jumpa!{Colors.ENDC}\n")