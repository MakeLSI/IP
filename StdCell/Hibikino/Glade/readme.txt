Glade�p�Ђт��̐݌v�֘A�t�@�C��(akita11)

Glade�́A���C�A�E�g���H�݌v�̂��߂�CAD�B�t���[�E�G�A�ŁAWin/Mac/Linux�Ή��B�Ƃ���ǂ���o�O�����邪�A�قƂ�ǂ͖��Ȃ��g���A�C���������B
http://www.peardrop.co.uk/

��Glade�̃O���b�h���̐ݒ�
�Ђт��̐݌v���[���ł́A���W�̍ŏ��P�ʂ�1um�Ȃ̂ŁA�ŏ���DisplayOptions(E)�̒���DisplaySettings�ŁADisplayGridSettings��X,Y�Ƃ���1.0[um]�ɁASnapSettings��SnapGrid��X,Y�Ƃ���1.0[um]�ɐݒ肵�Ă����B

���X�^���_�[�h�Z���̎g����
1. https://github.com/MakeLSI/IP ����t�@�C�����ꎮ�_�E�����[�h���ēW�J����B���̒���Hibikino/Glade�ȉ����A�Ђт��̌�����Glade�p�X�^�Z���B
2. Glade��Open->Library����A�W�J�t�H���_����StdCell���w��Binv1�Ȃǂ̘_���Q�[�g��layout, symbol, schematic������͂��B
3. �V�K�ɐ݌v�p�̃��C�u�������AFile->New Lib�Ń��C�u�������쐬�B���̂Ƃ��ATechnology��hibikino.tch���w�肷��i�����Ń��C����`�Ȃǂ��ݒ肳���j�B����H�}�쐬�͈ȉ����Q��
4. �V����schematics��layout�̃Z���������āA������StdCell����X�^�Z��(�_���Q�[�g)�AP-Cell�Ȃǂ��Ăяo���āA�Ȃ��ŉ�H������B�u�Ăяo���v�́A�C���X�^���X�쐬(i)����A�Ăяo���X�^�Z�����w�肷��ƁA���̃X�^�Z���������̉�H�̒��ɒu�����B��P-Cell�ɂ��Ă͈ȉ����Q�ƁB�܂��Ăяo���X�^�Z����StdCell�̒��̂��̂��w�肷�邱�Ɓi�����̉�H�̃��C�u�����ɃR�s�[���Ă���g��Ȃ��j
5. DRC��LVS�Ō��؂���

��DRC�̂�������
Verify->DRC->Run DRC (Shift+D)�ŁA"hibikino-drc.py" ���w�肵��DRC��������B
�G���[�������Verify->DRC->View DRC Errors�Ŋm�F�ł���

����H���o�̎g����
Verify->Extract->RunLVE�ŁA"hibikino-ext.py"���w�肷��ƁA���̃Z���ɑ΂���extracted�Ƃ����r���[���ł���B�E����"Net Browser"�ɁA�l�b�g��������A�ǂꂩ��I������ƁA���̃l�b�g�ɑΉ�����I�u�W�F�N�g���n�C���C�g�����B�Ȃ����C�A�E�g�ŁAML1/ML2/POL�ɓ������C���ŏ�����������i������̐���_���Ώې}�`�̒��ɂ��邱�Ɓj���A���̃l�b�g�̃l�b�g���ɂȂ�B�l�b�g���X�g�t�@�C���̏o�͂́AFile->Export->Export CDL�ŁA�i�قځjspice�`���ŏo�͂ł���B

����H�}����
�EMOS��StdCell���̃Z��nch/pch���g���B
�E���o�͂́ACreate->Pin�Ńs���Ƃ��āA���̂����č쐬�B
�EVDD/GND���̓d���́A���o�͂Ɠ������s���Ƃ��č쐬����Bbasic���C�u��������vdd/gnd���g���Ă��悢���A�����̓f�t�H���g��net����vdd!/gnd!��"!"�����Ă��āA��X�̃l�b�g���̕s�����̌����ƂȂ�B
�E�����̒[�q�i�Ԃ��l�p�j��Wire�Ō��ԁB
�Ȃ�Wire�͍ŏ��̓l�b�g�������Ă��Ȃ����ACheck Cellview����ƃl�b�g�������B
�Ȃ����Ă���͂��Ȃ̂ɂȂ����Ă��Ȃ��i�����Ă���j�A�Ƃ����G���[���o�邱�Ƃ����邪�A�ēxCheck Cellview����Ǝ��邱�Ƃ�����i�䋓���j�B
�[�_��wire��2��ڂ��N���b�N����ƁAwire�z�����I���̂ŁA����łȂ����Ă��邩�͔��f�ł���i�[�_��ŃN���b�N���Ȃ���wire�z���������j�B
File->Export��Export CDL�Łi�قځjspice�`���̃l�b�g���X�g���o�͂ł���B

��LVS�̂�����
1.���C�A�E�g("layout")���J���A���̎菇�ŉ�H���o�B"extracted"�r���[�����������B
2."extracted"�r���[���J���A��������Verify->LVS->Run LVS��LVS�����s�B��ʂ̉E���Ł��ŉ�H�}����export�����l�b�g���X�g(CDL�`��)���w�肵�ALVS�����s�B���̂Ƃ��A
�K�w�\�������l�b�g���X�g�̏ꍇ��"Hierachical netlist?"���`�F�b�N����globa�l�b�g(�d���Ȃ�)�ƃg�b�v�̉�H(subckt)�����w�肷��B������ver4.5.24�ł́A���̂Ƃ��ɐ��������*.cdl_flat���ɁA�g�����W�X�^�T�C�Y�̒P�ʂ��w�肷��u*.SCALE METER�v�������o����Ȃ����߁A��x*.cdl_flat�𐶐���A"*.SCALE METER"��ǋL���A���߂�"Hierachical netlist?"�̃`�F�b�N���͂�����LVS��������΃g�����W�X�^�T�C�Y���`�F�b�N��OK�B

��P-Cell
P-Cell(parameterized cell)�Ƃ́AMOS�g�����W�X�^�Ȃǂ̗v�f���i���A���̌`��p�����[�^�i�Q�[�g���Ȃǁj���w�肵�āA�����I�Ƀ��C�A�E�g���쐬����@�\�B
(1)nMOS/pMOS�p
1.nmos_master.py��pmos_master.py���ǂ����ɒu���A���ϐ�PYTHONPATH���A���̃f�B���N�g���ɐݒ肷��i�Ȃ��ꍇ�͍쐬�A���ɂ���ꍇ�͒ǉ��j�B�܂��͂�����Glade�̃f�B���N�g��(�E�E�E/glade_win64/�Ȃ�)�ɒu���B
2.New->Cell��Cell���쐬����Ƃ��A"CellView is a Pcell"���`�F�b�N���A"Pcell script"�ɁA������*.py���w�肵�AOK����ƁAnmos_master�܂���nmos_master��layout���쐬�����B�����̃T�C�Y�͕W���l�ō쐬�����B�i���̃Z����super master�ƌĂԁj
3.�g�������Z��(layout)�ŁA�C���X�^���X�쐬(i)�ŁACellName��h_nmos�܂���h_pmos��I�сA ���̂Ƃ�"Instance Property"�^�u�ŁAl�i�Q�[�g���j�Aw�i�Q�[�g���j�Am�i�t�B���K�[���j�Apoly_con�i�Q�[�g�ɃR���^�N�g��ł��j���w�肵�ăC���X�^���X���쐬����ƁA���̃p�����[�^�̐��@��MOS�g�����W�X�^���u�����B�i���܂��쐬����Ȃ��ꍇ������悤�����A��������쐬��A�C���X�^���X�̃v���p�e�B���炱���̃p�����[�^���C������΁A����ɉ������T�C�Y��MOS�g�����W�X�^�ɂȂ�j

(2)�R���^�N�g�EVIA�p
�ȉ��̂��̂�����B����������E�c�ɕ��ׂ�R���^�N�gorVIA�̌���nx,ny�Ŏw�肷��B
�Epolycon_master.py : POL-ML1+�R���^�N�g(CNP)
�Encon_master.py : nACT-ML1+�R���^�N�g(CNA)
�Epcon_master.py : pACT-ML1+�R���^�N�g(CNA)
�Eml1via_master.py : ML1-ML2+VIA

��Glade���상��
�EDisplayOption->Miscellaneous��Always pop up option dialog���͂����ƁAMove�Ȃǂ̂��тɃI�v�V������ʂ��\������Ȃ��iF3�œK�X�\���ł���j
�Eschematic/symbol���J������Ԃ�CheckCellview����ƁAMOSFET�̃C���X�^���X�̓Z�����̐擪��M(spice��MOSFET������킷)�ȂǁA�����őf�q���ɑΉ��������̂ɂȂ�B�����DisplayOptions->ObjectSettings�ɂ���"InstanceNames"��Preserve�ɂ���ƁA�����ŕύX����Ȃ��ł���B


----------------------------------------
�X�^�Z���쐬���̎w�j
StdCell���C�u�������J���A�����̃X�^�Z��(inv1.gex�Ȃ�)�ɑ΂��āA�ȉ��̏C���E�ǉ����s���Ă����B
�E���̂̕ύX(������_v2.gex�����Binv1_v2.gex -> inv1 �Ȃ�)
�Elayout�ł̐M�������x��������̕ύX�i���͂�IA, IB, ...��I����n�܂�B�o�͂̓Q�[�g��O�A�t���b�v�t���b�v��Q��QB�j
�E��H�}(schematics)�̍쐬�i�M������layout�ɂ��킹��BnMOS/pMOS��StdCell���C�u��������nch/pch���A�d����bacis���C�u��������VDD/GND���g�p����j
�E�V���{��(symbol)�̍쐬�i�ȉ��̓_�ɗ���: inv1��symbol���Q�l�Ɂj
  - �K���Aschematics�쐬��create cellview from cellview�̗����symbol�p�̃Z�����쐬���A�����������ꂽ�s���͏����Ȃ�
    �������������ꂽ�s���������Ă��܂��ƁA�쐬����symbol�𑼂̃Z�����ŌĂяo�����ہA����symbol�Ƃ̐ڑ����F������Ȃ�(ver4.5.24�ł̊��m�̃o�O�ŏ����C���\��Ƃ̂���)
  - �O���b�h��1um�P�ʂƂ��āA���Ȃ��Ƃ��l�b�g�i�Ԃ��l�p�j�̓O���b�h�ɏ悹��i�\�Ȕ͈͂ł��ׂĂ̐}�`���j
  - �l�b�g����layout, schematics�ɂ��킹��
  - net�����Ƃ��́A���O���w�肷��i�󗓂ō쐬���Ă��Ƃ��疼�̕ύX�A���Ƃ��܂������Ȃ��ꍇ����j�B�Ȃ�net��Property�ł́AinstPin=1�ƂȂ��Ă���͂��B�inet����H�}�̃l�b�g�Apin=�V���{����̐ڑ��_�ŁA���҂͈�ʂɂ͈�v����j
  - �S�̂̑傫���́Ainv1�̂��̂�ڈ��Ɂi�ɒ[�ɑ傫��or�������Ȃ�Ȃ��悤�Ɂj
  - �S�̂̒��S���قڌ��_�ɗ���悤�ɔz�u����
  - cellName, instName�AText���쐬����"Label Use"��device label/inst label��I�сAsize��1.0��(������property��Label Type���A"NLPlabel"�ɂȂ�͂�)
  - (�\�Ȃ��)�g�����W�X�^���@���A"[@wp:wp=%:wp=18um]", "[@wn:wn=%:wn=6um]", "[@lp:lp=%:lp=2um]", "[@ln:ln=%:ln=2um]"��4���x��(annotate���C���ENLPlabel��)�ŏ����Ă����B
  - �V���{���`�掞�̉����I�����Ă��Ȃ���Ԃ�QueryProperty(Q)���炱�̃V���{���̃v���p�e�B��ݒ�ł���B�����ŁAProperty�^�u�ɁA�ȉ���2�̃v���p�e�B��ǉ��i��������^��string�A�l�̓��C�A�E�g�ɂ��킹�邪�X�^�Z���͊�{�I�ɂ��̐��@�̂͂��j
    * NLPDeviceFormat -> [@instName] [|I:%] [|O:%] inv [@wp:wp=%:wp=18u] [@wn:wn=%:wn=6u] [@lp:lp=%:lp=2u] [@ln:ln=%:ln=2u]
    * defaultParams -> wp=16u wn=6u lp=2u ln=2u
  - �O�g��boundary�̒����`�ň͂�
  - symbol���쐬������A�����I�����Ă��Ȃ���ԂŃZ����Property��\�������ANum Net��Num Pin���A�`�悵�Ă���[�q�̐��ƈ�v���Ă��邱�Ƃ��m�F����B
  - �ۑ��O��Check->CheckCellview�����ق��������B
���\�Ȃ�΁Aschematic��symbol�ŁAVDD/GND��basic�̃V���{���ł͂Ȃ�Pin�Ƃ��Ēu�������́iView���̖�����P������j���쐬(inv1���Q��)�B����͓d���d�����ʂȂǓd�����ʌn���̏ꍇ�Ɏg�p����B�Ȃ��ݒ��"NetUse"��POWER/GND���w�肷��B

