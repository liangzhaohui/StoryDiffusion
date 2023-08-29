import Vue from 'vue';
import VueI18n from 'vue-i18n';
import ElementUI from 'element-ui';
import elementEnLocale from 'element-ui/lib/locale/lang/en';

Vue.use(VueI18n);

const messages = {
    en: {
        ...elementEnLocale,
    },
};

const i18n = new VueI18n({
    locale: 'en',
    messages,
});

Vue.use(ElementUI, {
    i18n: (key, value) => i18n.t(key, value),
});

export default i18n;
