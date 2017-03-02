Glade用ひびきの設計関連ファイル(akita11)

Gladeは、レイアウトや回路設計のためのCAD。フリーウエアで、Win/Mac/Linux対応。ところどころバグがあるが、ほとんどは問題なく使え、修正も速い。
http://www.peardrop.co.uk/

○Gladeのグリッド等の設定
ひびきの設計ルールでは、座標の最小単位は1umなので、最初にDisplayOptions(E)の中のDisplaySettingsで、DisplayGridSettingsをX,Yともに1.0[um]に、SnapSettingsでSnapGridをX,Yともに1.0[um]に設定しておく。

○スタンダードセルの使い方
1. https://github.com/MakeLSI/IP からファイルを一式ダウンロードして展開する。この中のHibikino/Glade以下が、ひびきの向けのGlade用スタセル。
2. GladeのOpen->Libraryから、展開フォルダ内のStdCellを指定。inv1などの論理ゲートのlayout, symbol, schematicがあるはず。
3. 新規に設計用のライブラリを、File->New Libでライブラリを作成。このとき、Technologyでhibikino.tchを指定する（ここでレイヤ定義などが設定される）。※回路図作成は以下も参照
4. 新しいschematicsやlayoutのセルをつくって、そこにStdCellからスタセル(論理ゲート)、P-Cellなどを呼び出して、つないで回路をつくる。「呼び出し」は、インスタンス作成(i)から、呼び出すスタセルを指定すると、そのスタセルが自分の回路の中に置かれる。※P-Cellについては以下を参照。また呼び出すスタセルはStdCellの中のものを指定すること（自分の回路のライブラリにコピーしてから使わない）
5. DRCやLVSで検証する

○DRCのかけかた
Verify->DRC->Run DRC (Shift+D)で、"hibikino-drc.py" を指定してDRCをかける。
エラーがあればVerify->DRC->View DRC Errorsで確認できる

○回路抽出の使い方
Verify->Extract->RunLVEで、"hibikino-ext.py"を指定すると、そのセルに対してextractedというビューができる。右下の"Net Browser"に、ネット名が現れ、どれかを選択すると、そのネットに対応するオブジェクトがハイライトされる。なおレイアウトで、ML1/ML2/POLに同じレイヤで書いた文字列（文字列の制御点が対象図形の中にあること）が、そのネットのネット名になる。ネットリストファイルの出力は、File->Export->Export CDLで、（ほぼ）spice形式で出力できる。

○回路図入力
・MOSはStdCell内のセルnch/pchを使う。
・入出力は、Create->Pinでピンとして、名称をつけて作成。
・VDD/GND等の電源は、入出力と同じくピンとして作成する。basicライブラリ中のvdd/gndを使ってもよいが、これらはデフォルトのnet名がvdd!/gnd!と"!"がついていて、後々のネット名の不整合の原因となる。
・これらの端子（赤い四角）をWireで結ぶ。
なおWireは最初はネット名がついていないが、Check Cellviewするとネット名がつく。
つながっているはずなのにつながっていない（浮いている）、というエラーが出ることがあるが、再度Check Cellviewすると治ることもある（謎挙動）。
端点でwireの2回目をクリックすると、wire配線が終わるので、それでつながっているかは判断できる（端点上でクリックしないとwire配線が続く）。
File->Export→Export CDLで（ほぼ）spice形式のネットリストを出力できる。

○LVSのかけ方
1.レイアウト("layout")を開き、↑の手順で回路抽出。"extracted"ビューが生成される。
2."extracted"ビューを開き、そこからVerify->LVS->Run LVSでLVSを実行。画面の右側で↑で回路図からexportしたネットリスト(CDL形式)を指定し、LVSを実行。このとき、
階層構造を持つネットリストの場合は"Hierachical netlist?"をチェックしてglobaネット(電源など)とトップの回路(subckt)名を指定する。ただしver4.5.24では、このときに生成される*.cdl_flatがに、トランジスタサイズの単位を指定する「*.SCALE METER」が書き出されないため、一度*.cdl_flatを生成後、"*.SCALE METER"を追記し、改めて"Hierachical netlist?"のチェックをはずしてLVSをかければトランジスタサイズもチェックもOK。

○P-Cell
P-Cell(parameterized cell)とは、MOSトランジスタなどの要素部品を、その形状パラメータ（ゲート長など）を指定して、自動的にレイアウトを作成する機能。
(1)nMOS/pMOS用
1.nmos_master.pyとpmos_master.pyをどこかに置き、環境変数PYTHONPATHを、そのディレクトリに設定する（ない場合は作成、既にある場合は追加）。またはこれらをGladeのディレクトリ(・・・/glade_win64/など)に置く。
2.New->CellでCellを作成するとき、"CellView is a Pcell"をチェックし、"Pcell script"に、これらの*.pyを指定し、OKすると、nmos_masterまたはnmos_masterのlayoutが作成される。これらのサイズは標準値で作成される。（このセルをsuper masterと呼ぶ）
3.使いたいセル(layout)で、インスタンス作成(i)で、CellNameでh_nmosまたはh_pmosを選び、 そのとき"Instance Property"タブで、l（ゲート長）、w（ゲート幅）、m（フィンガー数）、poly_con（ゲートにコンタクトを打つか）を指定してインスタンスを作成すると、そのパラメータの寸法のMOSトランジスタが置かれる。（うまく作成されない場合があるようだが、いったん作成後、インスタンスのプロパティからこれらのパラメータを修正すれば、それに応じたサイズのMOSトランジスタになる）

(2)コンタクト・VIA用
以下のものがある。いずれも横・縦に並べるコンタクトorVIAの個数をnx,nyで指定する。
・polycon_master.py : POL-ML1+コンタクト(CNP)
・ncon_master.py : nACT-ML1+コンタクト(CNA)
・pcon_master.py : pACT-ML1+コンタクト(CNA)
・ml1via_master.py : ML1-ML2+VIA

※Glade操作メモ
・DisplayOption->MiscellaneousのAlways pop up option dialogをはずすと、Moveなどのたびにオプション画面が表示されない（F3で適宜表示できる）
・schematic/symbolを開いた状態でCheckCellviewすると、MOSFETのインスタンスはセル名の先頭がM(spiceでMOSFETをあらわす)など、自動で素子名に対応したものになる。これはDisplayOptions->ObjectSettingsにある"InstanceNames"をPreserveにすると、自動で変更されなくできる。


----------------------------------------
スタセル作成時の指針
StdCellライブラリを開き、既存のスタセル(inv1.gexなど)に対して、以下の修正・追加を行っていく。
・名称の変更(末尾の_v2.gexを取る。inv1_v2.gex -> inv1 など)
・layoutでの信号名ラベル文字列の変更（入力はIA, IB, ...とIから始まる。出力はゲートはO、フリップフロップはQとQB）
・回路図(schematics)の作成（信号名はlayoutにあわせる。nMOS/pMOSはStdCellライブラリ内のnch/pchを、電源はbacisライブラリ内のVDD/GNDを使用する）
・シンボル(symbol)の作成（以下の点に留意: inv1のsymbolを参考に）
  - 必ず、schematics作成→create cellview from cellviewの流れでsymbol用のセルを作成し、自動生成されたピンは消さない
    ※自動生成されたピンを消してしまうと、作成したsymbolを他のセル内で呼び出した際、他のsymbolとの接続が認識されない(ver4.5.24での既知のバグで将来修正予定とのこと)
  - グリッドは1um単位として、少なくともネット（赤い四角）はグリッドに乗せる（可能な範囲ですべての図形も）
  - ネット名はlayout, schematicsにあわせる
  - netを作るときは、名前を指定する（空欄で作成してあとから名称変更、だとうまくいかない場合あり）。なおnetのPropertyでは、instPin=1となっているはず。（net＝回路図のネット、pin=シンボル上の接続点で、両者は一般には一致する）
  - 全体の大きさは、inv1のものを目安に（極端に大きくor小さくならないように）
  - 全体の中心がほぼ原点に来るように配置する
  - cellName, instName、Textを作成時に"Label Use"をdevice label/inst labelを選び、sizeを1.0に(これらのpropertyのLabel Typeが、"NLPlabel"になるはず)
  - (可能ならば)トランジスタ寸法を、"[@wp:wp=%:wp=18um]", "[@wn:wn=%:wn=6um]", "[@lp:lp=%:lp=2um]", "[@ln:ln=%:ln=2um]"の4つラベル(annotateレイヤ・NLPlabelで)で書いておく。
  - シンボル描画時の何も選択していない状態でQueryProperty(Q)からこのシンボルのプロパティを設定できる。ここで、Propertyタブに、以下の2つのプロパティを追加（いずれも型はstring、値はレイアウトにあわせるがスタセルは基本的にこの寸法のはず）
    * NLPDeviceFormat -> [@instName] [|I:%] [|O:%] inv [@wp:wp=%:wp=18u] [@wn:wn=%:wn=6u] [@lp:lp=%:lp=2u] [@ln:ln=%:ln=2u]
    * defaultParams -> wp=16u wn=6u lp=2u ln=2u
  - 外枠をboundaryの長方形で囲う
  - symbolを作成したら、何も選択していない状態でセルのPropertyを表示させ、Num NetとNum Pinが、描画してある端子の数と一致していることを確認する。
  - 保存前にCheck->CheckCellviewしたほうがいい。
※可能ならば、schematicとsymbolで、VDD/GNDをbasicのシンボルではなくPinとして置いたもの（View名の末尾にPをつける）も作成(inv1を参照)。これは電源電圧が別など電源が別系統の場合に使用する。なお設定で"NetUse"でPOWER/GNDを指定する。

