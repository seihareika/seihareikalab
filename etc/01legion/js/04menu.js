$(".openbtn").click(function () {//�{�^�����N���b�N���ꂽ��
    $(this).toggleClass('active');//�{�^�����g�� active�N���X��t�^��
    $("#g-nav").toggleClass('panelactive');//�i�r�Q�[�V������panelactive�N���X��t�^
});

$("#g-nav a").click(function () {//�i�r�Q�[�V�����̃����N���N���b�N���ꂽ��
    $(".openbtn").removeClass('active');//�{�^���� active�N���X��������
    $("#g-nav").removeClass('panelactive');//�i�r�Q�[�V������panelactive�N���X������
});